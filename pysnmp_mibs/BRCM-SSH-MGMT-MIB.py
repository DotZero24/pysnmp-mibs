_L='sshHackerLastTime'
_K='sshHackerNumAttempts'
_J='seconds'
_I='accessible-for-notify'
_H='sshHackerAddress'
_G='sshHackerAddressType'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='BRCM-SSH-MGMT-MIB'
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
sshMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,4))
if mibBuilder.loadTexts:sshMgmt.setRevisions(('2007-02-05 00:00','2006-09-29 00:00','2006-02-02 00:00','2005-10-27 00:00'))
class _SshIpStackInterfaces_Type(Bits):defaultHexValue='00';namedValues=NamedValues(*(('interface1',0),('interface2',1),('interface3',2),('interface4',3),('interface5',4),('interface6',5),('interface7',6),('interface8',7)))
_SshIpStackInterfaces_Type.__name__='Bits'
_SshIpStackInterfaces_Object=MibScalar
sshIpStackInterfaces=_SshIpStackInterfaces_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,1),_SshIpStackInterfaces_Type())
sshIpStackInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:sshIpStackInterfaces.setStatus(_A)
class _SshUserName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SshUserName_Type.__name__=_F
_SshUserName_Object=MibScalar
sshUserName=_SshUserName_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,2),_SshUserName_Type())
sshUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sshUserName.setStatus(_A)
class _SshPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SshPassword_Type.__name__=_F
_SshPassword_Object=MibScalar
sshPassword=_SshPassword_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,3),_SshPassword_Type())
sshPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:sshPassword.setStatus(_A)
class _SshServerControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stop',0),('start',1)))
_SshServerControl_Type.__name__=_E
_SshServerControl_Object=MibScalar
sshServerControl=_SshServerControl_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,4),_SshServerControl_Type())
sshServerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:sshServerControl.setStatus(_A)
_SshSessionIp_Type=IpAddress
_SshSessionIp_Object=MibScalar
sshSessionIp=_SshSessionIp_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,5),_SshSessionIp_Type())
sshSessionIp.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionIp.setStatus('deprecated')
_SshSessionInProgress_Type=TruthValue
_SshSessionInProgress_Object=MibScalar
sshSessionInProgress=_SshSessionInProgress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,6),_SshSessionInProgress_Type())
sshSessionInProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionInProgress.setStatus(_A)
_SshForceUserLogout_Type=TruthValue
_SshForceUserLogout_Object=MibScalar
sshForceUserLogout=_SshForceUserLogout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,7),_SshForceUserLogout_Type())
sshForceUserLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:sshForceUserLogout.setStatus(_A)
_SshSessionAddressType_Type=InetAddressType
_SshSessionAddressType_Object=MibScalar
sshSessionAddressType=_SshSessionAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,8),_SshSessionAddressType_Type())
sshSessionAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionAddressType.setStatus(_A)
_SshSessionAddress_Type=InetAddress
_SshSessionAddress_Object=MibScalar
sshSessionAddress=_SshSessionAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,9),_SshSessionAddress_Type())
sshSessionAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionAddress.setStatus(_A)
_SshHackerTable_Object=MibTable
sshHackerTable=_SshHackerTable_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10))
if mibBuilder.loadTexts:sshHackerTable.setStatus(_A)
_SshHackerEntry_Object=MibTableRow
sshHackerEntry=_SshHackerEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10,1))
sshHackerEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:sshHackerEntry.setStatus(_A)
_SshHackerAddressType_Type=InetAddressType
_SshHackerAddressType_Object=MibTableColumn
sshHackerAddressType=_SshHackerAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10,1,1),_SshHackerAddressType_Type())
sshHackerAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:sshHackerAddressType.setStatus(_A)
_SshHackerAddress_Type=InetAddress
_SshHackerAddress_Object=MibTableColumn
sshHackerAddress=_SshHackerAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10,1,2),_SshHackerAddress_Type())
sshHackerAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:sshHackerAddress.setStatus(_A)
_SshHackerNumAttempts_Type=Unsigned32
_SshHackerNumAttempts_Object=MibTableColumn
sshHackerNumAttempts=_SshHackerNumAttempts_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10,1,3),_SshHackerNumAttempts_Type())
sshHackerNumAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:sshHackerNumAttempts.setStatus(_A)
_SshHackerLastTime_Type=TimeTicks
_SshHackerLastTime_Object=MibTableColumn
sshHackerLastTime=_SshHackerLastTime_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,10,1,4),_SshHackerLastTime_Type())
sshHackerLastTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sshHackerLastTime.setStatus(_A)
class _SshSessionInactivityTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_SshSessionInactivityTimeout_Type.__name__=_E
_SshSessionInactivityTimeout_Object=MibScalar
sshSessionInactivityTimeout=_SshSessionInactivityTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,11),_SshSessionInactivityTimeout_Type())
sshSessionInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sshSessionInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:sshSessionInactivityTimeout.setUnits(_J)
class _SshHackerInactivityTimeout_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,86400))
_SshHackerInactivityTimeout_Type.__name__=_E
_SshHackerInactivityTimeout_Object=MibScalar
sshHackerInactivityTimeout=_SshHackerInactivityTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,4,12),_SshHackerInactivityTimeout_Type())
sshHackerInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sshHackerInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:sshHackerInactivityTimeout.setUnits(_J)
_SshTraps_ObjectIdentity=ObjectIdentity
sshTraps=_SshTraps_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,4,99))
sshHackerTrap=NotificationType((1,3,6,1,4,1,4413,2,2,2,1,1,4,99,1))
sshHackerTrap.setObjects(*((_C,_G),(_C,_H),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:sshHackerTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sshMgmt':sshMgmt,'sshIpStackInterfaces':sshIpStackInterfaces,'sshUserName':sshUserName,'sshPassword':sshPassword,'sshServerControl':sshServerControl,'sshSessionIp':sshSessionIp,'sshSessionInProgress':sshSessionInProgress,'sshForceUserLogout':sshForceUserLogout,'sshSessionAddressType':sshSessionAddressType,'sshSessionAddress':sshSessionAddress,'sshHackerTable':sshHackerTable,'sshHackerEntry':sshHackerEntry,_G:sshHackerAddressType,_H:sshHackerAddress,_K:sshHackerNumAttempts,_L:sshHackerLastTime,'sshSessionInactivityTimeout':sshSessionInactivityTimeout,'sshHackerInactivityTimeout':sshHackerInactivityTimeout,'sshTraps':sshTraps,'sshHackerTrap':sshHackerTrap})