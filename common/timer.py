from concurrent.futures import ProcessPoolExecutor, _base, Future


def executeWithTimeOut(fnc, *args, **kwargs):
    with ProcessPoolExecutor() as p:
        try:
            f: Future = p.submit(fnc, *args, **kwargs)
            return f.result(timeout=10)
        except _base.TimeoutError:
            for pid, process in p._processes.items():
                process.terminate()
            p.shutdown()
            raise Exception('Process timed out.')