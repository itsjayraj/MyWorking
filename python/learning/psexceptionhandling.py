import sys
import traceback

def safe_float(args):
    try:
        value=None
        value = float(args[0]) / 0
    except ValueError, e:
        print(e)
    except (IndexError, KeyError), e:
        print(e)
    except:
        print(sys.exc_type)
        tb = sys.exc_info()[-1]
        traceback.print_tb(tb)
        print('internal script error')
    finally:
        print('am at finally block')
        return value


print(safe_float(123))