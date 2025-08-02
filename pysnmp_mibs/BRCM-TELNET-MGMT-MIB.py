_L='telnetHackerLastTime'
_K='telnetHackerNumAttempts'
_J='seconds'
_I='accessible-for-notify'
_H='telnetHackerAddress'
_G='telnetHackerAddressType'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='BRCM-TELNET-MGMT-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtBase,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtBase')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TruthValue')
telnetMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,1))
if mibBuilder.loadTexts:telnetMgmt.setRevisions(('2007-02-05 00:00','2006-09-29 00:00','2006-02-02 00:00','2005-06-08 00:00','2003-03-06 00:00'))
class _TelnetIpStackInterfaces_Type(Bits):defaultHexValue='00';namedValues=NamedValues(*(('interface1',0),('interface2',1),('interface3',2),('interface4',3),('interface5',4),('interface6',5),('interface7',6),('interface8',7)))
_TelnetIpStackInterfaces_Type.__name__='Bits'
_TelnetIpStackInterfaces_Object=MibScalar
telnetIpStackInterfaces=_TelnetIpStackInterfaces_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,1),_TelnetIpStackInterfaces_Type())
telnetIpStackInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetIpStackInterfaces.setStatus(_A)
class _TelnetUserName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TelnetUserName_Type.__name__=_F
_TelnetUserName_Object=MibScalar
telnetUserName=_TelnetUserName_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,2),_TelnetUserName_Type())
telnetUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserName.setStatus(_A)
class _TelnetPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_TelnetPassword_Type.__name__=_F
_TelnetPassword_Object=MibScalar
telnetPassword=_TelnetPassword_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,3),_TelnetPassword_Type())
telnetPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetPassword.setStatus(_A)
class _TelnetServerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stop',0),('start',1)))
_TelnetServerControl_Type.__name__=_E
_TelnetServerControl_Object=MibScalar
telnetServerControl=_TelnetServerControl_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,4),_TelnetServerControl_Type())
telnetServerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetServerControl.setStatus(_A)
_TelnetSessionIp_Type=IpAddress
_TelnetSessionIp_Object=MibScalar
telnetSessionIp=_TelnetSessionIp_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,5),_TelnetSessionIp_Type())
telnetSessionIp.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetSessionIp.setStatus('deprecated')
_TelnetSessionInProgress_Type=TruthValue
_TelnetSessionInProgress_Object=MibScalar
telnetSessionInProgress=_TelnetSessionInProgress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,6),_TelnetSessionInProgress_Type())
telnetSessionInProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetSessionInProgress.setStatus(_A)
_TelnetForceUserLogout_Type=TruthValue
_TelnetForceUserLogout_Object=MibScalar
telnetForceUserLogout=_TelnetForceUserLogout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,7),_TelnetForceUserLogout_Type())
telnetForceUserLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetForceUserLogout.setStatus(_A)
_TelnetSessionAddressType_Type=InetAddressType
_TelnetSessionAddressType_Object=MibScalar
telnetSessionAddressType=_TelnetSessionAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,8),_TelnetSessionAddressType_Type())
telnetSessionAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetSessionAddressType.setStatus(_A)
_TelnetSessionAddress_Type=InetAddress
_TelnetSessionAddress_Object=MibScalar
telnetSessionAddress=_TelnetSessionAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,9),_TelnetSessionAddress_Type())
telnetSessionAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetSessionAddress.setStatus(_A)
_TelnetHackerTable_Object=MibTable
telnetHackerTable=_TelnetHackerTable_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10))
if mibBuilder.loadTexts:telnetHackerTable.setStatus(_A)
_TelnetHackerEntry_Object=MibTableRow
telnetHackerEntry=_TelnetHackerEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10,1))
telnetHackerEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:telnetHackerEntry.setStatus(_A)
_TelnetHackerAddressType_Type=InetAddressType
_TelnetHackerAddressType_Object=MibTableColumn
telnetHackerAddressType=_TelnetHackerAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10,1,1),_TelnetHackerAddressType_Type())
telnetHackerAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:telnetHackerAddressType.setStatus(_A)
_TelnetHackerAddress_Type=InetAddress
_TelnetHackerAddress_Object=MibTableColumn
telnetHackerAddress=_TelnetHackerAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10,1,2),_TelnetHackerAddress_Type())
telnetHackerAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:telnetHackerAddress.setStatus(_A)
_TelnetHackerNumAttempts_Type=Unsigned32
_TelnetHackerNumAttempts_Object=MibTableColumn
telnetHackerNumAttempts=_TelnetHackerNumAttempts_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10,1,3),_TelnetHackerNumAttempts_Type())
telnetHackerNumAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetHackerNumAttempts.setStatus(_A)
_TelnetHackerLastTime_Type=TimeTicks
_TelnetHackerLastTime_Object=MibTableColumn
telnetHackerLastTime=_TelnetHackerLastTime_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,10,1,4),_TelnetHackerLastTime_Type())
telnetHackerLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetHackerLastTime.setStatus(_A)
class _TelnetSessionInactivityTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_TelnetSessionInactivityTimeout_Type.__name__=_E
_TelnetSessionInactivityTimeout_Object=MibScalar
telnetSessionInactivityTimeout=_TelnetSessionInactivityTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,11),_TelnetSessionInactivityTimeout_Type())
telnetSessionInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetSessionInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:telnetSessionInactivityTimeout.setUnits(_J)
class _TelnetHackerInactivityTimeout_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,86400))
_TelnetHackerInactivityTimeout_Type.__name__=_E
_TelnetHackerInactivityTimeout_Object=MibScalar
telnetHackerInactivityTimeout=_TelnetHackerInactivityTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,1,12),_TelnetHackerInactivityTimeout_Type())
telnetHackerInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetHackerInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:telnetHackerInactivityTimeout.setUnits(_J)
_TelnetTraps_ObjectIdentity=ObjectIdentity
telnetTraps=_TelnetTraps_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,1,99))
telnetHackerTrap=NotificationType((1,3,6,1,4,1,4413,2,2,2,1,1,1,99,1))
telnetHackerTrap.setObjects(*((_C,_G),(_C,_H),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:telnetHackerTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'telnetMgmt':telnetMgmt,'telnetIpStackInterfaces':telnetIpStackInterfaces,'telnetUserName':telnetUserName,'telnetPassword':telnetPassword,'telnetServerControl':telnetServerControl,'telnetSessionIp':telnetSessionIp,'telnetSessionInProgress':telnetSessionInProgress,'telnetForceUserLogout':telnetForceUserLogout,'telnetSessionAddressType':telnetSessionAddressType,'telnetSessionAddress':telnetSessionAddress,'telnetHackerTable':telnetHackerTable,'telnetHackerEntry':telnetHackerEntry,_G:telnetHackerAddressType,_H:telnetHackerAddress,_K:telnetHackerNumAttempts,_L:telnetHackerLastTime,'telnetSessionInactivityTimeout':telnetSessionInactivityTimeout,'telnetHackerInactivityTimeout':telnetHackerInactivityTimeout,'telnetTraps':telnetTraps,'telnetHackerTrap':telnetHackerTrap})