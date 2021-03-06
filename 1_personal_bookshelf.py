# =============================================================================
#       *****In the Name of God*****
#          zahra.kh2005@gmail.com
#       Author Name : Zahra khalifeh-zadeh
#         Code Name : Maktab51-HW5
# =============================================================================

"""
This code suggest for creat personal Zahra_bookshelf.
in this code we use base sample for bookshelf but we can also add other media types instance to the bookshelf.

Note1: first should install "terminaltables" module in pycharm for show output in table format,
or use commented show_bookshelf() and sort_bookshelf() function for show output in lines format.

Note2: a pdf-file is attached to show the output report
"""
from terminaltables import AsciiTable


class MediaType:
    def __init__(self, media_type, title, author, publish_year, pages, language, price, issue=None, speaker=None,
                 time=None, book_language=None, audio_language=None, current=0, progress=0, status=None, remaining=0):
        """
        :param media_type: type's of all media instance
        :param title: title's of all media instance
        :param author: author's of  book, magazine and audiobook instance
        :param publish_year: publish_year's of all media instance
        :param pages: number of pages from  of book, magazine and audiobook instance
        :param language: language's of book, magazine and Podcast instance
        :param price: price's of all media instance
        :param issue: issue's of Magazine instance
        :param speaker: speaker's of Podcast and Audiobook instance
        :param time: time's of Podcast and Audiobook instance
        :param book_language: book_language's of Audiobook instance
        :param audio_language: audio_language's of Audiobook instance
        :param current: current page/time of all media instance
        :param progress: progress's of all media instance
        :param status: status's of all media instance
        :param remaining: remain page/time of all media instance
        """
        self.media_type = media_type
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.issue = issue
        self.speaker = speaker
        self.time = time
        self.book_language = book_language
        self.audio_language = audio_language
        self.current = current
        self.progress = progress
        self.status = status
        self.remaining = remaining

    def read(self):
        """
            This function update current_page  for book and magazine instance.
            and define ???progress??? as percent of pages which has been read for each media.
        """
        self.current = MediaType.get_current_page_time(self)
        self.progress = round((self.current / self.pages * 100), 2)
        if self.current == self.pages:
            print(f'You completed the {self.media_type}_{self.title}')
        elif self.current > self.pages:
            print(f'You can not read more than {self.pages}_pages.enter new current page or enter "0" to exit.')
            self.current = MediaType.get_current_page_time(self)
            self.progress = round((self.current / self.pages * 100), 2)
            if self.current == self.pages:
                print(f'You completed the {self.media_type}_{self.title}')
            elif self.current < self.pages:
                self.remaining = self.pages - self.current
                print(f'"you have read {self.current} more pages from {self.media_type}_{self.title}.'
                      f'There are {self.remaining} pages left"')
        else:
            self.remaining = self.pages - self.current
            print(f'"you have read {self.current} more pages from {self.media_type}_{self.title}.'
                  f'There are {self.remaining} pages left"')
        return self.current

    def listen(self):
        """
            This function update current_time for Podcast and Audiobook instance
            and define ???progress??? as percent of time which has been listened for each media.
        """
        self.current = MediaType.get_current_page_time(self)
        self.progress = round((self.current / self.time * 100), 2)
        if self.current == self.time:
            print(f'You completed the {self.media_type}_{self.title}')
        elif self.current > self.time:
            print(f'You can not listen more than {self.time}_times.enter new current time or enter "0" to exit.')
            self.current = MediaType.get_current_page_time(self)
            self.progress = round((self.current / self.time * 100), 2)
            if self.current == self.time:
                print(f'You completed the {self.media_type}_{self.title}')
            elif self.current < self.time:
                self.remaining = self.time - self.current
                print(f'"you have listen {self.current} more times from '
                      f'{self.media_type}_{self.title}.There are {self.remaining} times left"')
        else:
            self.remaining = self.time - self.current
            print(f'"you have listen {self.current} more times from '
                  f'{self.media_type}_{self.title}.There are {self.remaining} times left"')
        return self.current

    def get_status(self):
        """
            this function set status for every object
            unread : no pages/time has been read/listen yet
            reading : reading/listening the book/Audio
            finished : all pages/time has been read/listen
        """
        if self.media_type == 'Book' or self.media_type == "Magazine":
            if self.current == 0:
                self.status = 'unread'
            elif self.current < self.pages:
                self.status = 'reading'
            elif self.current == self.pages:
                self.status = 'finished'
        elif self.media_type == 'Podcast' or self.media_type == 'Audiobook':
            if self.current == 0:
                self.status = 'unread'
            elif self.current < self.time:
                self.status = 'reading'
            elif self.current == self.time:
                self.status = 'finished'
        return self.status

    def get_current_page_time(self):
        """
            This function handle ValueError: invalid literal for int() with base 10
        """
        try:
            self.current = int(input(f'enter your current page/time for {self.media_type}_{self.title}: '))
        except ValueError:
            print('You did not enter a number!')
            self.current = int(input(f'enter your current page/time for {self.media_type}_{self.title}: '))
        return self.current

    @staticmethod
    def get_int_float_data(metric_input, metric_num):
        """
        This function handle ValueError: invalid literal for int() with base 10
        :param metric_input: attribute for instance
        :param metric_num: int/float
        """
        try:
            metric_input = metric_num(input(f'{metric_input}:'))
        except ValueError:
            print('You did not enter a number!')
            metric_input = metric_num(input(f'{metric_input}:'))
        return metric_input

    def __str__(self):
        """print information of each class instance"""
        return f'MediaType: {self.media_type}, title: {self.title},' \
               f' publish_year: {self.publish_year}, price: {self.price} $'


# ####################################### end base class #############################################################

class Book(MediaType):
    def __init__(self, title, author, publish_year, pages, language, price):
        super().__init__('Book', title, author, publish_year, pages, language, price)

    @staticmethod
    def get_data():
        """
        get data from input and make a book instance from that information And add books to the bookshelf
        :return: book_instance
        """
        print(f'enter information for book:')
        title = input('title:')
        author = input('author:')
        language = input('Language:')
        publish_year = MediaType.get_int_float_data('publish_year', int)
        pages = MediaType.get_int_float_data('pages', int)
        price = MediaType.get_int_float_data('price', float)
        book_instance = Book(title, author, publish_year, pages, language, price)
        return book_instance

    def __str__(self):
        return super().__str__() + f', author(s): {self.author}, pages: {self.pages}, language: {self.language}'


class Magazine(MediaType):
    def __init__(self, title, author, publish_year, pages, language, price, issue):
        super().__init__('Magazine', title, author, publish_year, pages, language, price, issue)

    @staticmethod
    def get_data():
        """
        get data from input and make a magazine instance from that information And add Magazines to the bookshelf
        :return: magazine_instance
        """
        print(f'enter information for Magazine:')
        title = input('title:')
        author = input('author:')
        language = input('Language:')
        publish_year = MediaType.get_int_float_data('publish_year', int)
        pages = MediaType.get_int_float_data('pages', int)
        price = MediaType.get_int_float_data('price', float)
        issue = MediaType.get_int_float_data('issue', float)
        magazine_instance = Magazine(title, author, publish_year, pages, language, price, issue)
        return magazine_instance

    def __str__(self):
        return super().__str__() + f', author(s): {self.author}, pages: {self.pages},' \
                                   f' language: {self.language}, issue:{self.issue}'


class Podcast(MediaType):
    def __init__(self, title, speaker, publish_year, time, language, price):
        super().__init__('Podcast', title, speaker, publish_year, time, language, price)
        self.speaker = speaker
        self.time = time

    @staticmethod
    def get_data():
        """
        get data from input and make a podcast instance from that information And add podcast to the bookshelf
        :return: podcast_instance
        """
        print(f'enter information for Podcast:')
        title = input('title:')
        speaker = input('speaker:')
        language = input('Language:')
        publish_year = MediaType.get_int_float_data('publish_year', int)
        price = MediaType.get_int_float_data('price', float)
        time = MediaType.get_int_float_data('time', int)
        podcast_instance = Podcast(title, speaker, publish_year, time, language, price)
        return podcast_instance

    def __str__(self):
        return super().__str__() + f', speaker: {self.speaker}, language: {self.language}, time: {self.time}'


class Audiobook(MediaType):
    def __init__(self, title, speaker, author, publish_year, pages, book_language, audio_language, time, price):
        super().__init__('Audiobook', title, speaker, author, publish_year, pages, book_language, price)
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.price = price
        self.speaker = speaker
        self.book_language = book_language
        self.audio_language = audio_language
        self.time = time

    @staticmethod
    def get_data():
        """
        get data from input and make a audiobook instance from that information And add audiobook to the bookshelf
        :return: Audiobook_instance
        """
        print(f'enter information for Audiobook:')
        title = input('title:')
        speaker = input('speaker:')
        author = input('author:')
        book_language = input('book_language:')
        audio_language = input('audio_language:')
        publish_year = MediaType.get_int_float_data('publish_year', int)
        price = MediaType.get_int_float_data('price', float)
        time = MediaType.get_int_float_data('time', int)
        pages = MediaType.get_int_float_data('pages', int)
        audiobook_instance = Audiobook(title, speaker, author, publish_year, pages, book_language, audio_language, time,
                                       price)
        return audiobook_instance

    def __str__(self):
        return super().__str__() + f', author(s): {self.author}, book_language:  {self.book_language}, ' \
                                   f'speaker: {self.speaker}, audio_language: {self.audio_language}, time: {self.time}'


# ############################################# end define classes ####################################################
# #####################################################################################################################

# ############################################# functions in menu #####################################################
bookshelf = []
sample = [['Book', 'No Friend But the Mountains', 'Behrouz Boochani', 2018, 374, 'English', 10],
          ['Book', 'The Black Swan', 'Abbas Maroufi', 2007, 280, 'Persian', 20],
          ['Book', 'Symphony of the Dead', 'Behrouz Boochani', 2018, 374, 'English', 126],
          ['Magazine', 'Bukhara', '[Ali Dehbashi,Darioush Ashoori]', 2020, 768, 'Persian', 55, 140],
          ['Podcast', 'Ravaaq', 'Farzin.Ranjbar', 2020, 50, 'Persian', 0],
          ['Audiobook', 'The Black Swan', 'Ali Bandari', 'Nassim.Nicholas.Taleb', 2020, 400, 'English', 'Persian', 62,
           0]]

""" we can add sample instance to empty bookshelf """
for lst in sample:
    if lst[0] == 'Book':
        book = Book(*lst[1:7])
        bookshelf.append(book)
    elif lst[0] == 'Magazine':
        magazine = Magazine(*lst[1:8])
        bookshelf.append(magazine)
    elif lst[0] == 'Podcast':
        podcast = Podcast(*lst[1:7])
        bookshelf.append(podcast)
    elif lst[0] == 'Audiobook':
        audiobook = Audiobook(*lst[1:10])
        bookshelf.append(audiobook)


def add_media():
    """
        add other media types instance to the bookshelf
    """
    media_type = input('Enter B/M/P/A for get info (B=Book/M=Magazine/P=Podcast/A=Audiobook): ')
    if media_type == 'B':
        my_book = Book.get_data()
        bookshelf.append(my_book)
    if media_type == 'M':
        my_magazine = Magazine.get_data()
        bookshelf.append(my_magazine)
    if media_type == 'P':
        my_podcast = Podcast.get_data()
        bookshelf.append(my_podcast)
    if media_type == 'A':
        my_audiobook = Audiobook.get_data()
        bookshelf.append(my_audiobook)


""" show bookshelf in line format """


# def show_bookshelf():
#     for item in bookshelf:
#         print(bookshelf.index(item) + 1, item, f', status: {item.status}')  # index start from 1


def show_bookshelf():
    """
        show bookshelf in table format
        Note: first should install terminaltables in pycharm / or use commented function show_bookshelf() above
    """
    total_row = []
    table_column_headers = ["ID", "media_type", "title", "author(s)", "pages", "time", "current", "progress", "status",
                            "price", "publish_year", "issue", "speaker", "language", "book_language", "audio_language"]

    total_row.append(table_column_headers)
    for item in bookshelf:
        item_id = bookshelf.index(item) + 1
        if item.media_type == 'Book':
            book_row = [item_id, item.media_type, item.title, item.author, item.pages, '', f'page_{item.current}',
                        f'{item.progress} %', item.status, f'{item.price} $', item.publish_year, '', '', item.language,
                        '', '']
            total_row.append(book_row)
        elif item.media_type == 'Magazine':
            magazine_row = [item_id, item.media_type, item.title, item.author, item.pages, '', f'page_{item.current}',
                            f'{item.progress} %', item.status, f'{item.price} $', item.publish_year, item.issue, '',
                            item.language, '', '']
            total_row.append(magazine_row)
        elif item.media_type == 'Podcast':
            podcast_row = [item_id, item.media_type, item.title, '', '', f'{item.time} min', f'min_{item.current}',
                           f'{item.progress} %', item.status, f'{item.price} $', item.publish_year, '', item.speaker,
                           item.language, '', '']
            total_row.append(podcast_row)
        elif item.media_type == 'Audiobook':
            audiobook_row = [item_id, item.media_type, item.title, item.author, item.pages, f'{item.time} min',
                             f'min_{item.current}', f'{item.progress} %', item.status, f'{item.price} $',
                             item.publish_year, '', item.speaker, '', item.book_language, item.audio_language]
            total_row.append(audiobook_row)
    data = total_row
    table = AsciiTable(data)
    print(table.table)


def read_listen(my_choice_id):
    """
    :param my_choice_id: choice id from media type in bookshelf
    :return: current_page/time  from media type and get status
    """
    for elem in bookshelf:
        if bookshelf.index(elem) == my_choice_id - 1:  # because index start from zero
            _id = my_choice_id - 1
            my_datatype = bookshelf[_id].media_type
            if my_datatype == 'Book':
                Book.read(bookshelf[_id])
                Book.get_status(bookshelf[_id])
            elif my_datatype == 'Magazine':
                Magazine.read(bookshelf[_id])
                Magazine.get_status(bookshelf[_id])
            elif my_datatype == 'Podcast':
                Podcast.listen(bookshelf[_id])
                Podcast.get_status(bookshelf[_id])
            elif my_datatype == 'Audiobook':
                Audiobook.listen(bookshelf[_id])
                Audiobook.get_status(bookshelf[_id])


def add_read_listen():
    """
        this function call read/listen method for media type which choice id
    """
    show_bookshelf()
    print('Enter "id" from above table to add read page or time listen.')
    my_choice_id = MediaType.get_int_float_data('my choice id: ', int)
    if my_choice_id in range(1, len(bookshelf) + 1):
        read_listen(my_choice_id)
    else:
        print(f'Please enter True "id" from  range (1 - {len(bookshelf)}): ')
        my_choice_id = MediaType.get_int_float_data('my choice id: ', int)
        if my_choice_id in range(1, len(bookshelf) + 1):
            read_listen(my_choice_id)


def ranking(list_input, Metric, reverse, count=None):
    """
    This function get Metric argument for show sort list_input base on Metric=progress
    :return: sorted list by progress
    """
    list_input = sorted(list_input, key=lambda x: x.__getattribute__(Metric), reverse=reverse)
    return list_input[:count]


"""
This function show sorted bookshelf based on progress in line format
"""


# def sort_bookshelf():
#     sort_by_progress = ranking(bookshelf, 'progress', True)
#     for item in sort_by_progress:
#         print(f'{item.media_type}_{item.title}, progress = {item.progress} %')


def sort_bookshelf():
    """
        This function show sorted bookshelf based on progress in table format
        Note: first should install terminaltables in pycharm / or use commented function sort_bookshelf() above
    """
    total_row_sort = []
    table_column_headers = ["media_type", "title", "progress"]
    total_row_sort.append(table_column_headers)
    sort_by_progress = ranking(bookshelf, 'progress', True)

    for item in sort_by_progress:
        if item.media_type == 'Book':
            book_row = [item.media_type, item.title, f'{item.progress} %']
            total_row_sort.append(book_row)
        elif item.media_type == 'Magazine':
            magazine_row = [item.media_type, item.title, f'{item.progress} %']
            total_row_sort.append(magazine_row)
        elif item.media_type == 'Podcast':
            podcast_row = [item.media_type, item.title, f'{item.progress} %']
            total_row_sort.append(podcast_row)
        elif item.media_type == 'Audiobook':
            audiobook_row = [item.media_type, item.title, f'{item.progress} %']
            total_row_sort.append(audiobook_row)
    data = total_row_sort
    table = AsciiTable(data)
    print(table.table)


# ##################################### Run menu and choice what do you do? ###########################################
def print_menu():
    print("************ Welcome to Zahra_Bookshelf ***************")
    print("""what do you do?\t
    1: Add a Book/Magazine/PodcastEpisode/Audiobook\t
    2: Show my bookshelf\t
    3: Add read page or time listen\t
    4: Sort my bookshelf\t
    5: Quit\t""")


def main():
    print_menu()
    choice = 0
    while choice != "5":
        choice = input("Please enter your choice:")
        if choice == "1":
            add_media()
            print_menu()
        elif choice == "2":
            show_bookshelf()
            print_menu()
        elif choice == "3":
            add_read_listen()
            print_menu()
        elif choice == "4":
            sort_bookshelf()
            print_menu()
        elif choice == "5":
            print("\n******  Goodbye Zahra  ******")
        else:
            print("Invalid choice. Please try again.")


"""Run program by show menu"""
main()
