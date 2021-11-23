import os

def Console():
    guilds = len(Rise.guilds)
    print(f'''{Fore.WHITE}
{Fore.WHITE}     {Fore.BLUE}██████╗{Fore.WHITE}  {Fore.RED}█████╗{Fore.WHITE}  {Fore.YELLOW}█████╗{Fore.WHITE}  {Fore.BLUE}██████╗{Fore.WHITE} {Fore.GREEN}██╗{Fore.WHITE}     {Fore.RED}███████╗{Fore.WHITE}  ██████╗  █████╗ ████████╗    
{Fore.WHITE}    {Fore.BLUE}██╔════╝{Fore.WHITE} {Fore.RED}██╔══██╗{Fore.YELLOW}██╔══██╗{Fore.BLUE}██╔════╝{Fore.WHITE} {Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}██╔════╝{Fore.WHITE}  ██╔══██╗██╔══██╗╚══██╔══╝    
{Fore.WHITE}    {Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}██╗{Fore.WHITE} {Fore.RED}██║{Fore.WHITE}  {Fore.RED}██║{Fore.YELLOW}██║{Fore.WHITE}  {Fore.YELLOW}██║{Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}██╗{Fore.WHITE} {Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}█████╗{Fore.WHITE}    ██████╦╝██║  ██║   ██║       
{Fore.WHITE}    {Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}╚██╗{Fore.RED}██║{Fore.WHITE}  {Fore.RED}██║{Fore.YELLOW}██║{Fore.WHITE}  {Fore.YELLOW}██║{Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}╚██╗{Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}██╔══╝{Fore.WHITE}    ██╔══██╗██║  ██║   ██║       
{Fore.WHITE}    {Fore.BLUE}╚██████╔╝{Fore.RED}╚█████╔╝{Fore.YELLOW}╚█████╔╝{Fore.BLUE}╚██████╔╝{Fore.GREEN}███████╗{Fore.RED}███████╗{Fore.WHITE}  ██████╦╝╚█████╔╝   ██║       
{Fore.WHITE}     {Fore.BLUE}╚═════╝{Fore.WHITE}  {Fore.RED}╚════╝{Fore.WHITE}  {Fore.YELLOW}╚════╝{Fore.WHITE}  {Fore.BLUE}╚═════╝{Fore.WHITE} {Fore.GREEN}╚══════╝{Fore.RED}╚══════╝{Fore.WHITE}  ╚═════╝  ╚════╝    ╚═╝       
                                Don't Be Evil
                                        Use RiseSB
{Fore.RESET} ''')
    print(f'{Style.BRIGHT}' + f'{Fore.RED}' 'Connected: '  + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + f'{Rise.user.name}' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + '#' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + f'{Rise.user.discriminator}' 
    + f'{Style.BRIGHT}' + f'{Fore.RED}' ' Prefix: ' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + '[' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + f'{prefix}' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + ']'
    + f'{Style.BRIGHT}' + f'{Fore.RED}' ' Servers: ' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' + f'{guilds}'  )
    print(f'{Fore.WHITE}' '═' * os.get_terminal_size().columns)
    print(f'{Style.BRIGHT}' + f'{Fore.RED}' 'Hint: Type' + f'{Style.BRIGHT}' + f'{Fore.WHITE}' ' help ' + f'{Style.BRIGHT}' + f'{Fore.RED}' 'in console to see all console commands.' )

os.system('mode con: cols=85 lines=25')

    
Console()
