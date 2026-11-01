import main_core
if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main_core.main())
    except KeyboardInterrupt:
        pass
