_J='zySysLogServerInetAddress'
_I='zySysLogServerInetAddressType'
_H='read-only'
_G='zySysLogTypeIndex'
_F='InetAddress'
_E='not-accessible'
_D='ZYXEL-SYSLOG-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSysLog=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,81))
_ZyxelSysLogSetup_ObjectIdentity=ObjectIdentity
zyxelSysLogSetup=_ZyxelSysLogSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,81,1))
_ZySysLogState_Type=EnabledStatus
_ZySysLogState_Object=MibScalar
zySysLogState=_ZySysLogState_Object((1,3,6,1,4,1,890,1,15,3,81,1,1),_ZySysLogState_Type())
zySysLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysLogState.setStatus(_A)
_ZyxelSysLogTypeTable_Object=MibTable
zyxelSysLogTypeTable=_ZyxelSysLogTypeTable_Object((1,3,6,1,4,1,890,1,15,3,81,1,2))
if mibBuilder.loadTexts:zyxelSysLogTypeTable.setStatus(_A)
_ZyxelSysLogTypeEntry_Object=MibTableRow
zyxelSysLogTypeEntry=_ZyxelSysLogTypeEntry_Object((1,3,6,1,4,1,890,1,15,3,81,1,2,1))
zyxelSysLogTypeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:zyxelSysLogTypeEntry.setStatus(_A)
_ZySysLogTypeIndex_Type=Integer32
_ZySysLogTypeIndex_Object=MibTableColumn
zySysLogTypeIndex=_ZySysLogTypeIndex_Object((1,3,6,1,4,1,890,1,15,3,81,1,2,1,1),_ZySysLogTypeIndex_Type())
zySysLogTypeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysLogTypeIndex.setStatus(_A)
_ZySysLogTypeName_Type=DisplayString
_ZySysLogTypeName_Object=MibTableColumn
zySysLogTypeName=_ZySysLogTypeName_Object((1,3,6,1,4,1,890,1,15,3,81,1,2,1,2),_ZySysLogTypeName_Type())
zySysLogTypeName.setMaxAccess(_H)
if mibBuilder.loadTexts:zySysLogTypeName.setStatus(_A)
_ZySysLogTypeState_Type=EnabledStatus
_ZySysLogTypeState_Object=MibTableColumn
zySysLogTypeState=_ZySysLogTypeState_Object((1,3,6,1,4,1,890,1,15,3,81,1,2,1,3),_ZySysLogTypeState_Type())
zySysLogTypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysLogTypeState.setStatus(_A)
class _ZySysLogTypeFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('localUser0',0),('localUser1',1),('localUser2',2),('localUser3',3),('localUser4',4),('localUser5',5),('localUser6',6),('localUser7',7)))
_ZySysLogTypeFacility_Type.__name__=_C
_ZySysLogTypeFacility_Object=MibTableColumn
zySysLogTypeFacility=_ZySysLogTypeFacility_Object((1,3,6,1,4,1,890,1,15,3,81,1,2,1,4),_ZySysLogTypeFacility_Type())
zySysLogTypeFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysLogTypeFacility.setStatus(_A)
_ZySysLogMaxNumberOfServers_Type=Integer32
_ZySysLogMaxNumberOfServers_Object=MibScalar
zySysLogMaxNumberOfServers=_ZySysLogMaxNumberOfServers_Object((1,3,6,1,4,1,890,1,15,3,81,1,3),_ZySysLogMaxNumberOfServers_Type())
zySysLogMaxNumberOfServers.setMaxAccess(_H)
if mibBuilder.loadTexts:zySysLogMaxNumberOfServers.setStatus(_A)
_ZyxelSysLogServerInetTable_Object=MibTable
zyxelSysLogServerInetTable=_ZyxelSysLogServerInetTable_Object((1,3,6,1,4,1,890,1,15,3,81,1,5))
if mibBuilder.loadTexts:zyxelSysLogServerInetTable.setStatus(_A)
_ZyxelSysLogServerInetEntry_Object=MibTableRow
zyxelSysLogServerInetEntry=_ZyxelSysLogServerInetEntry_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1))
zyxelSysLogServerInetEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:zyxelSysLogServerInetEntry.setStatus(_A)
_ZySysLogServerInetAddressType_Type=InetAddressType
_ZySysLogServerInetAddressType_Object=MibTableColumn
zySysLogServerInetAddressType=_ZySysLogServerInetAddressType_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1,1),_ZySysLogServerInetAddressType_Type())
zySysLogServerInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysLogServerInetAddressType.setStatus(_A)
class _ZySysLogServerInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZySysLogServerInetAddress_Type.__name__=_F
_ZySysLogServerInetAddress_Object=MibTableColumn
zySysLogServerInetAddress=_ZySysLogServerInetAddress_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1,2),_ZySysLogServerInetAddress_Type())
zySysLogServerInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysLogServerInetAddress.setStatus(_A)
class _ZySysLogServerInetLogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('level0',0),('level0To1',1),('level0To2',2),('level0To3',3),('level0To4',4),('level0To5',5),('level0To6',6),('level0To7',7)))
_ZySysLogServerInetLogLevel_Type.__name__=_C
_ZySysLogServerInetLogLevel_Object=MibTableColumn
zySysLogServerInetLogLevel=_ZySysLogServerInetLogLevel_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1,3),_ZySysLogServerInetLogLevel_Type())
zySysLogServerInetLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysLogServerInetLogLevel.setStatus(_A)
class _ZySysLogServerInetUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZySysLogServerInetUdpPort_Type.__name__=_C
_ZySysLogServerInetUdpPort_Object=MibTableColumn
zySysLogServerInetUdpPort=_ZySysLogServerInetUdpPort_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1,4),_ZySysLogServerInetUdpPort_Type())
zySysLogServerInetUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysLogServerInetUdpPort.setStatus(_A)
_ZySysLogServerInetRowStatus_Type=RowStatus
_ZySysLogServerInetRowStatus_Object=MibTableColumn
zySysLogServerInetRowStatus=_ZySysLogServerInetRowStatus_Object((1,3,6,1,4,1,890,1,15,3,81,1,5,1,5),_ZySysLogServerInetRowStatus_Type())
zySysLogServerInetRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zySysLogServerInetRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelSysLog':zyxelSysLog,'zyxelSysLogSetup':zyxelSysLogSetup,'zySysLogState':zySysLogState,'zyxelSysLogTypeTable':zyxelSysLogTypeTable,'zyxelSysLogTypeEntry':zyxelSysLogTypeEntry,_G:zySysLogTypeIndex,'zySysLogTypeName':zySysLogTypeName,'zySysLogTypeState':zySysLogTypeState,'zySysLogTypeFacility':zySysLogTypeFacility,'zySysLogMaxNumberOfServers':zySysLogMaxNumberOfServers,'zyxelSysLogServerInetTable':zyxelSysLogServerInetTable,'zyxelSysLogServerInetEntry':zyxelSysLogServerInetEntry,_I:zySysLogServerInetAddressType,_J:zySysLogServerInetAddress,'zySysLogServerInetLogLevel':zySysLogServerInetLogLevel,'zySysLogServerInetUdpPort':zySysLogServerInetUdpPort,'zySysLogServerInetRowStatus':zySysLogServerInetRowStatus})