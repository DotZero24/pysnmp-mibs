_X='hm2TrackOperState'
_W='hm2TrackStatus'
_V='hm2TrackInterfaceStatusEntry'
_U='hm2TrackStaticRouteEntry'
_T='hm2TrackAppId'
_S='hm2TrackLogicalId'
_R='milliseconds'
_Q='hm2TrackPingId'
_P='seconds'
_O='hm2TrackInterfaceId'
_N='accessible-for-notify'
_M='HmEnabledStatus'
_L='notReady'
_K='down'
_J='InterfaceIndexOrZero'
_I='not-accessible'
_H='read-create'
_G='hm2TrackId'
_F='hm2TrackType'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='HM2-TRACKING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_M,'HmTimeSeconds1970','hm2ConfigurationMibs')
InterfaceIndexOrZero,ifEntry=mibBuilder.importSymbols('IF-MIB',_J,'ifEntry')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
inetCidrRouteEntry,=mibBuilder.importSymbols('IP-FORWARD-MIB','inetCidrRouteEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hm2TrackingMib=ModuleIdentity((1,3,6,1,4,1,248,11,115))
if mibBuilder.loadTexts:hm2TrackingMib.setRevisions(('2022-11-24 12:00','2013-09-03 12:00'))
_Hm2TrackingMibNotifications_ObjectIdentity=ObjectIdentity
hm2TrackingMibNotifications=_Hm2TrackingMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,115,0))
_Hm2TrackingMibObjects_ObjectIdentity=ObjectIdentity
hm2TrackingMibObjects=_Hm2TrackingMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,115,1))
_Hm2TrackingConfigGroup_ObjectIdentity=ObjectIdentity
hm2TrackingConfigGroup=_Hm2TrackingConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,1))
_Hm2TrackingConfigTable_Object=MibTable
hm2TrackingConfigTable=_Hm2TrackingConfigTable_Object((1,3,6,1,4,1,248,11,115,1,1,1))
if mibBuilder.loadTexts:hm2TrackingConfigTable.setStatus(_A)
_Hm2TrackingConfigEntry_Object=MibTableRow
hm2TrackingConfigEntry=_Hm2TrackingConfigEntry_Object((1,3,6,1,4,1,248,11,115,1,1,1,1))
hm2TrackingConfigEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hm2TrackingConfigEntry.setStatus(_A)
class _Hm2TrackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('interface',1),('ping',2),('logical',3)))
_Hm2TrackType_Type.__name__=_D
_Hm2TrackType_Object=MibTableColumn
hm2TrackType=_Hm2TrackType_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,1),_Hm2TrackType_Type())
hm2TrackType.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2TrackType.setStatus(_A)
class _Hm2TrackId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Hm2TrackId_Type.__name__=_D
_Hm2TrackId_Object=MibTableColumn
hm2TrackId=_Hm2TrackId_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,2),_Hm2TrackId_Type())
hm2TrackId.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2TrackId.setStatus(_A)
_Hm2TrackName_Type=SnmpAdminString
_Hm2TrackName_Object=MibTableColumn
hm2TrackName=_Hm2TrackName_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,3),_Hm2TrackName_Type())
hm2TrackName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackName.setStatus(_A)
_Hm2TrackDescription_Type=SnmpAdminString
_Hm2TrackDescription_Object=MibTableColumn
hm2TrackDescription=_Hm2TrackDescription_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,4),_Hm2TrackDescription_Type())
hm2TrackDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2TrackDescription.setStatus(_A)
class _Hm2TrackOperState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_K,2),(_L,3)))
_Hm2TrackOperState_Type.__name__=_D
_Hm2TrackOperState_Object=MibTableColumn
hm2TrackOperState=_Hm2TrackOperState_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,5),_Hm2TrackOperState_Type())
hm2TrackOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackOperState.setStatus(_A)
_Hm2TrackNumberOfChanges_Type=Integer32
_Hm2TrackNumberOfChanges_Object=MibTableColumn
hm2TrackNumberOfChanges=_Hm2TrackNumberOfChanges_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,6),_Hm2TrackNumberOfChanges_Type())
hm2TrackNumberOfChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackNumberOfChanges.setStatus(_A)
_Hm2TrackTimeLastChange_Type=HmTimeSeconds1970
_Hm2TrackTimeLastChange_Object=MibTableColumn
hm2TrackTimeLastChange=_Hm2TrackTimeLastChange_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,7),_Hm2TrackTimeLastChange_Type())
hm2TrackTimeLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackTimeLastChange.setStatus(_A)
class _Hm2TrackSendStateChangeTrap_Type(HmEnabledStatus):defaultValue=2
_Hm2TrackSendStateChangeTrap_Type.__name__=_M
_Hm2TrackSendStateChangeTrap_Object=MibTableColumn
hm2TrackSendStateChangeTrap=_Hm2TrackSendStateChangeTrap_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,8),_Hm2TrackSendStateChangeTrap_Type())
hm2TrackSendStateChangeTrap.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2TrackSendStateChangeTrap.setStatus(_A)
_Hm2TrackStatus_Type=RowStatus
_Hm2TrackStatus_Object=MibTableColumn
hm2TrackStatus=_Hm2TrackStatus_Object((1,3,6,1,4,1,248,11,115,1,1,1,1,9),_Hm2TrackStatus_Type())
hm2TrackStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2TrackStatus.setStatus(_A)
_Hm2TrackingInterfaceGroup_ObjectIdentity=ObjectIdentity
hm2TrackingInterfaceGroup=_Hm2TrackingInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,2))
_Hm2TrackingInterfaceTable_Object=MibTable
hm2TrackingInterfaceTable=_Hm2TrackingInterfaceTable_Object((1,3,6,1,4,1,248,11,115,1,2,1))
if mibBuilder.loadTexts:hm2TrackingInterfaceTable.setStatus(_A)
_Hm2TrackingInterfaceEntry_Object=MibTableRow
hm2TrackingInterfaceEntry=_Hm2TrackingInterfaceEntry_Object((1,3,6,1,4,1,248,11,115,1,2,1,1))
hm2TrackingInterfaceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:hm2TrackingInterfaceEntry.setStatus(_A)
_Hm2TrackInterfaceId_Type=Integer32
_Hm2TrackInterfaceId_Object=MibTableColumn
hm2TrackInterfaceId=_Hm2TrackInterfaceId_Object((1,3,6,1,4,1,248,11,115,1,2,1,1,1),_Hm2TrackInterfaceId_Type())
hm2TrackInterfaceId.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrackInterfaceId.setStatus(_A)
class _Hm2TrackIfNumber_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2TrackIfNumber_Type.__name__=_J
_Hm2TrackIfNumber_Object=MibTableColumn
hm2TrackIfNumber=_Hm2TrackIfNumber_Object((1,3,6,1,4,1,248,11,115,1,2,1,1,2),_Hm2TrackIfNumber_Type())
hm2TrackIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackIfNumber.setStatus(_A)
class _Hm2TrackIfLinkUpDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2TrackIfLinkUpDelay_Type.__name__=_D
_Hm2TrackIfLinkUpDelay_Object=MibTableColumn
hm2TrackIfLinkUpDelay=_Hm2TrackIfLinkUpDelay_Object((1,3,6,1,4,1,248,11,115,1,2,1,1,3),_Hm2TrackIfLinkUpDelay_Type())
hm2TrackIfLinkUpDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackIfLinkUpDelay.setStatus(_A)
if mibBuilder.loadTexts:hm2TrackIfLinkUpDelay.setUnits(_P)
class _Hm2TrackIfLinkDownDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2TrackIfLinkDownDelay_Type.__name__=_D
_Hm2TrackIfLinkDownDelay_Object=MibTableColumn
hm2TrackIfLinkDownDelay=_Hm2TrackIfLinkDownDelay_Object((1,3,6,1,4,1,248,11,115,1,2,1,1,4),_Hm2TrackIfLinkDownDelay_Type())
hm2TrackIfLinkDownDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackIfLinkDownDelay.setStatus(_A)
if mibBuilder.loadTexts:hm2TrackIfLinkDownDelay.setUnits(_P)
_Hm2TrackingPingGroup_ObjectIdentity=ObjectIdentity
hm2TrackingPingGroup=_Hm2TrackingPingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,3))
_Hm2TrackingPingTable_Object=MibTable
hm2TrackingPingTable=_Hm2TrackingPingTable_Object((1,3,6,1,4,1,248,11,115,1,3,1))
if mibBuilder.loadTexts:hm2TrackingPingTable.setStatus(_A)
_Hm2TrackingPingEntry_Object=MibTableRow
hm2TrackingPingEntry=_Hm2TrackingPingEntry_Object((1,3,6,1,4,1,248,11,115,1,3,1,1))
hm2TrackingPingEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:hm2TrackingPingEntry.setStatus(_A)
_Hm2TrackPingId_Type=Integer32
_Hm2TrackPingId_Object=MibTableColumn
hm2TrackPingId=_Hm2TrackPingId_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,1),_Hm2TrackPingId_Type())
hm2TrackPingId.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrackPingId.setStatus(_A)
class _Hm2TrackPingIfNumber_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2TrackPingIfNumber_Type.__name__=_J
_Hm2TrackPingIfNumber_Object=MibTableColumn
hm2TrackPingIfNumber=_Hm2TrackPingIfNumber_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,2),_Hm2TrackPingIfNumber_Type())
hm2TrackPingIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingIfNumber.setStatus(_A)
_Hm2TrackPingInetAddrType_Type=InetAddressType
_Hm2TrackPingInetAddrType_Object=MibTableColumn
hm2TrackPingInetAddrType=_Hm2TrackPingInetAddrType_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,3),_Hm2TrackPingInetAddrType_Type())
hm2TrackPingInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingInetAddrType.setStatus(_A)
_Hm2TrackPingInetAddr_Type=InetAddress
_Hm2TrackPingInetAddr_Object=MibTableColumn
hm2TrackPingInetAddr=_Hm2TrackPingInetAddr_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,4),_Hm2TrackPingInetAddr_Type())
hm2TrackPingInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingInetAddr.setStatus(_A)
class _Hm2TrackPingInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,20000))
_Hm2TrackPingInterval_Type.__name__=_D
_Hm2TrackPingInterval_Object=MibTableColumn
hm2TrackPingInterval=_Hm2TrackPingInterval_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,5),_Hm2TrackPingInterval_Type())
hm2TrackPingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingInterval.setStatus(_A)
if mibBuilder.loadTexts:hm2TrackPingInterval.setUnits(_R)
class _Hm2TrackPingMiss_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Hm2TrackPingMiss_Type.__name__=_D
_Hm2TrackPingMiss_Object=MibTableColumn
hm2TrackPingMiss=_Hm2TrackPingMiss_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,6),_Hm2TrackPingMiss_Type())
hm2TrackPingMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingMiss.setStatus(_A)
class _Hm2TrackPingSuccess_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Hm2TrackPingSuccess_Type.__name__=_D
_Hm2TrackPingSuccess_Object=MibTableColumn
hm2TrackPingSuccess=_Hm2TrackPingSuccess_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,7),_Hm2TrackPingSuccess_Type())
hm2TrackPingSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingSuccess.setStatus(_A)
class _Hm2TrackPingTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_Hm2TrackPingTimeout_Type.__name__=_D
_Hm2TrackPingTimeout_Object=MibTableColumn
hm2TrackPingTimeout=_Hm2TrackPingTimeout_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,8),_Hm2TrackPingTimeout_Type())
hm2TrackPingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:hm2TrackPingTimeout.setUnits(_R)
class _Hm2TrackPingTTL_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2TrackPingTTL_Type.__name__=_D
_Hm2TrackPingTTL_Object=MibTableColumn
hm2TrackPingTTL=_Hm2TrackPingTTL_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,9),_Hm2TrackPingTTL_Type())
hm2TrackPingTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackPingTTL.setStatus(_A)
_Hm2TrackPingBestRouteIfNumber_Type=InterfaceIndexOrZero
_Hm2TrackPingBestRouteIfNumber_Object=MibTableColumn
hm2TrackPingBestRouteIfNumber=_Hm2TrackPingBestRouteIfNumber_Object((1,3,6,1,4,1,248,11,115,1,3,1,1,10),_Hm2TrackPingBestRouteIfNumber_Type())
hm2TrackPingBestRouteIfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackPingBestRouteIfNumber.setStatus(_A)
_Hm2TrackingLogicalGroup_ObjectIdentity=ObjectIdentity
hm2TrackingLogicalGroup=_Hm2TrackingLogicalGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,4))
_Hm2TrackLogicalInstanceTable_Object=MibTable
hm2TrackLogicalInstanceTable=_Hm2TrackLogicalInstanceTable_Object((1,3,6,1,4,1,248,11,115,1,4,1))
if mibBuilder.loadTexts:hm2TrackLogicalInstanceTable.setStatus(_A)
_Hm2TrackLogicalInstanceEntry_Object=MibTableRow
hm2TrackLogicalInstanceEntry=_Hm2TrackLogicalInstanceEntry_Object((1,3,6,1,4,1,248,11,115,1,4,1,1))
hm2TrackLogicalInstanceEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hm2TrackLogicalInstanceEntry.setStatus(_A)
_Hm2TrackLogicalId_Type=Integer32
_Hm2TrackLogicalId_Object=MibTableColumn
hm2TrackLogicalId=_Hm2TrackLogicalId_Object((1,3,6,1,4,1,248,11,115,1,4,1,1,1),_Hm2TrackLogicalId_Type())
hm2TrackLogicalId.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrackLogicalId.setStatus(_A)
_Hm2TrackLogicalOperandNameA_Type=SnmpAdminString
_Hm2TrackLogicalOperandNameA_Object=MibTableColumn
hm2TrackLogicalOperandNameA=_Hm2TrackLogicalOperandNameA_Object((1,3,6,1,4,1,248,11,115,1,4,1,1,2),_Hm2TrackLogicalOperandNameA_Type())
hm2TrackLogicalOperandNameA.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackLogicalOperandNameA.setStatus(_A)
_Hm2TrackLogicalOperandNameB_Type=SnmpAdminString
_Hm2TrackLogicalOperandNameB_Object=MibTableColumn
hm2TrackLogicalOperandNameB=_Hm2TrackLogicalOperandNameB_Object((1,3,6,1,4,1,248,11,115,1,4,1,1,3),_Hm2TrackLogicalOperandNameB_Type())
hm2TrackLogicalOperandNameB.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackLogicalOperandNameB.setStatus(_A)
class _Hm2TrackLogicalOperator_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_Hm2TrackLogicalOperator_Type.__name__=_D
_Hm2TrackLogicalOperator_Object=MibTableColumn
hm2TrackLogicalOperator=_Hm2TrackLogicalOperator_Object((1,3,6,1,4,1,248,11,115,1,4,1,1,4),_Hm2TrackLogicalOperator_Type())
hm2TrackLogicalOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackLogicalOperator.setStatus(_A)
_Hm2TrackingApplicationGroup_ObjectIdentity=ObjectIdentity
hm2TrackingApplicationGroup=_Hm2TrackingApplicationGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,5))
_Hm2TrackingApplicationTable_Object=MibTable
hm2TrackingApplicationTable=_Hm2TrackingApplicationTable_Object((1,3,6,1,4,1,248,11,115,1,5,1))
if mibBuilder.loadTexts:hm2TrackingApplicationTable.setStatus(_A)
_Hm2TrackingApplicationEntry_Object=MibTableRow
hm2TrackingApplicationEntry=_Hm2TrackingApplicationEntry_Object((1,3,6,1,4,1,248,11,115,1,5,1,1))
hm2TrackingApplicationEntry.setIndexNames((0,_B,_T),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hm2TrackingApplicationEntry.setStatus(_A)
_Hm2TrackAppId_Type=Integer32
_Hm2TrackAppId_Object=MibTableColumn
hm2TrackAppId=_Hm2TrackAppId_Object((1,3,6,1,4,1,248,11,115,1,5,1,1,1),_Hm2TrackAppId_Type())
hm2TrackAppId.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrackAppId.setStatus(_A)
_Hm2TrackAppName_Type=SnmpAdminString
_Hm2TrackAppName_Object=MibTableColumn
hm2TrackAppName=_Hm2TrackAppName_Object((1,3,6,1,4,1,248,11,115,1,5,1,1,4),_Hm2TrackAppName_Type())
hm2TrackAppName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackAppName.setStatus(_A)
_Hm2TrackAppObjectName_Type=SnmpAdminString
_Hm2TrackAppObjectName_Object=MibTableColumn
hm2TrackAppObjectName=_Hm2TrackAppObjectName_Object((1,3,6,1,4,1,248,11,115,1,5,1,1,5),_Hm2TrackAppObjectName_Type())
hm2TrackAppObjectName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackAppObjectName.setStatus(_A)
_Hm2TrackingStaticRouteGroup_ObjectIdentity=ObjectIdentity
hm2TrackingStaticRouteGroup=_Hm2TrackingStaticRouteGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,6))
_Hm2TrackStaticRouteTable_Object=MibTable
hm2TrackStaticRouteTable=_Hm2TrackStaticRouteTable_Object((1,3,6,1,4,1,248,11,115,1,6,1))
if mibBuilder.loadTexts:hm2TrackStaticRouteTable.setStatus(_A)
_Hm2TrackStaticRouteEntry_Object=MibTableRow
hm2TrackStaticRouteEntry=_Hm2TrackStaticRouteEntry_Object((1,3,6,1,4,1,248,11,115,1,6,1,1))
if mibBuilder.loadTexts:hm2TrackStaticRouteEntry.setStatus(_A)
_Hm2TrackStaticRouteTrackId_Type=SnmpAdminString
_Hm2TrackStaticRouteTrackId_Object=MibTableColumn
hm2TrackStaticRouteTrackId=_Hm2TrackStaticRouteTrackId_Object((1,3,6,1,4,1,248,11,115,1,6,1,1,1),_Hm2TrackStaticRouteTrackId_Type())
hm2TrackStaticRouteTrackId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2TrackStaticRouteTrackId.setStatus(_A)
class _Hm2TrackStaticRouteTrackState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_K,2),(_L,3)))
_Hm2TrackStaticRouteTrackState_Type.__name__=_D
_Hm2TrackStaticRouteTrackState_Object=MibTableColumn
hm2TrackStaticRouteTrackState=_Hm2TrackStaticRouteTrackState_Object((1,3,6,1,4,1,248,11,115,1,6,1,1,2),_Hm2TrackStaticRouteTrackState_Type())
hm2TrackStaticRouteTrackState.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackStaticRouteTrackState.setStatus(_A)
_Hm2TrackingSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2TrackingSNMPExtensionGroup=_Hm2TrackingSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,7))
_Hm2TrackingInvalidTrackID_ObjectIdentity=ObjectIdentity
hm2TrackingInvalidTrackID=_Hm2TrackingInvalidTrackID_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,7,1))
if mibBuilder.loadTexts:hm2TrackingInvalidTrackID.setStatus(_A)
_Hm2TrackingTrackNameRegistrationErrorReturn_ObjectIdentity=ObjectIdentity
hm2TrackingTrackNameRegistrationErrorReturn=_Hm2TrackingTrackNameRegistrationErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,7,2))
if mibBuilder.loadTexts:hm2TrackingTrackNameRegistrationErrorReturn.setStatus(_A)
_Hm2TrackingTrackNameDeregisterationErrorReturn_ObjectIdentity=ObjectIdentity
hm2TrackingTrackNameDeregisterationErrorReturn=_Hm2TrackingTrackNameDeregisterationErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,7,3))
if mibBuilder.loadTexts:hm2TrackingTrackNameDeregisterationErrorReturn.setStatus(_A)
_Hm2TrackingInterfaceStatusGroup_ObjectIdentity=ObjectIdentity
hm2TrackingInterfaceStatusGroup=_Hm2TrackingInterfaceStatusGroup_ObjectIdentity((1,3,6,1,4,1,248,11,115,1,8))
_Hm2TrackInterfaceStatusTable_Object=MibTable
hm2TrackInterfaceStatusTable=_Hm2TrackInterfaceStatusTable_Object((1,3,6,1,4,1,248,11,115,1,8,1))
if mibBuilder.loadTexts:hm2TrackInterfaceStatusTable.setStatus(_A)
_Hm2TrackInterfaceStatusEntry_Object=MibTableRow
hm2TrackInterfaceStatusEntry=_Hm2TrackInterfaceStatusEntry_Object((1,3,6,1,4,1,248,11,115,1,8,1,1))
if mibBuilder.loadTexts:hm2TrackInterfaceStatusEntry.setStatus(_A)
_Hm2TrackInterfaceStatusTrackId_Type=SnmpAdminString
_Hm2TrackInterfaceStatusTrackId_Object=MibTableColumn
hm2TrackInterfaceStatusTrackId=_Hm2TrackInterfaceStatusTrackId_Object((1,3,6,1,4,1,248,11,115,1,8,1,1,1),_Hm2TrackInterfaceStatusTrackId_Type())
hm2TrackInterfaceStatusTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2TrackInterfaceStatusTrackId.setStatus(_A)
class _Hm2TrackInterfaceStatusTrackState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_K,2),(_L,3)))
_Hm2TrackInterfaceStatusTrackState_Type.__name__=_D
_Hm2TrackInterfaceStatusTrackState_Object=MibTableColumn
hm2TrackInterfaceStatusTrackState=_Hm2TrackInterfaceStatusTrackState_Object((1,3,6,1,4,1,248,11,115,1,8,1,1,2),_Hm2TrackInterfaceStatusTrackState_Type())
hm2TrackInterfaceStatusTrackState.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2TrackInterfaceStatusTrackState.setStatus(_A)
inetCidrRouteEntry.registerAugmentions((_B,_U))
hm2TrackStaticRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
ifEntry.registerAugmentions((_B,_V))
hm2TrackInterfaceStatusEntry.setIndexNames(*ifEntry.getIndexNames())
hm2TrackStatusChangeEvent=NotificationType((1,3,6,1,4,1,248,11,115,0,1))
hm2TrackStatusChangeEvent.setObjects(*((_B,_F),(_B,_G),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hm2TrackStatusChangeEvent.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hm2TrackingMib':hm2TrackingMib,'hm2TrackingMibNotifications':hm2TrackingMibNotifications,'hm2TrackStatusChangeEvent':hm2TrackStatusChangeEvent,'hm2TrackingMibObjects':hm2TrackingMibObjects,'hm2TrackingConfigGroup':hm2TrackingConfigGroup,'hm2TrackingConfigTable':hm2TrackingConfigTable,'hm2TrackingConfigEntry':hm2TrackingConfigEntry,_F:hm2TrackType,_G:hm2TrackId,'hm2TrackName':hm2TrackName,'hm2TrackDescription':hm2TrackDescription,_X:hm2TrackOperState,'hm2TrackNumberOfChanges':hm2TrackNumberOfChanges,'hm2TrackTimeLastChange':hm2TrackTimeLastChange,'hm2TrackSendStateChangeTrap':hm2TrackSendStateChangeTrap,_W:hm2TrackStatus,'hm2TrackingInterfaceGroup':hm2TrackingInterfaceGroup,'hm2TrackingInterfaceTable':hm2TrackingInterfaceTable,'hm2TrackingInterfaceEntry':hm2TrackingInterfaceEntry,_O:hm2TrackInterfaceId,'hm2TrackIfNumber':hm2TrackIfNumber,'hm2TrackIfLinkUpDelay':hm2TrackIfLinkUpDelay,'hm2TrackIfLinkDownDelay':hm2TrackIfLinkDownDelay,'hm2TrackingPingGroup':hm2TrackingPingGroup,'hm2TrackingPingTable':hm2TrackingPingTable,'hm2TrackingPingEntry':hm2TrackingPingEntry,_Q:hm2TrackPingId,'hm2TrackPingIfNumber':hm2TrackPingIfNumber,'hm2TrackPingInetAddrType':hm2TrackPingInetAddrType,'hm2TrackPingInetAddr':hm2TrackPingInetAddr,'hm2TrackPingInterval':hm2TrackPingInterval,'hm2TrackPingMiss':hm2TrackPingMiss,'hm2TrackPingSuccess':hm2TrackPingSuccess,'hm2TrackPingTimeout':hm2TrackPingTimeout,'hm2TrackPingTTL':hm2TrackPingTTL,'hm2TrackPingBestRouteIfNumber':hm2TrackPingBestRouteIfNumber,'hm2TrackingLogicalGroup':hm2TrackingLogicalGroup,'hm2TrackLogicalInstanceTable':hm2TrackLogicalInstanceTable,'hm2TrackLogicalInstanceEntry':hm2TrackLogicalInstanceEntry,_S:hm2TrackLogicalId,'hm2TrackLogicalOperandNameA':hm2TrackLogicalOperandNameA,'hm2TrackLogicalOperandNameB':hm2TrackLogicalOperandNameB,'hm2TrackLogicalOperator':hm2TrackLogicalOperator,'hm2TrackingApplicationGroup':hm2TrackingApplicationGroup,'hm2TrackingApplicationTable':hm2TrackingApplicationTable,'hm2TrackingApplicationEntry':hm2TrackingApplicationEntry,_T:hm2TrackAppId,'hm2TrackAppName':hm2TrackAppName,'hm2TrackAppObjectName':hm2TrackAppObjectName,'hm2TrackingStaticRouteGroup':hm2TrackingStaticRouteGroup,'hm2TrackStaticRouteTable':hm2TrackStaticRouteTable,_U:hm2TrackStaticRouteEntry,'hm2TrackStaticRouteTrackId':hm2TrackStaticRouteTrackId,'hm2TrackStaticRouteTrackState':hm2TrackStaticRouteTrackState,'hm2TrackingSNMPExtensionGroup':hm2TrackingSNMPExtensionGroup,'hm2TrackingInvalidTrackID':hm2TrackingInvalidTrackID,'hm2TrackingTrackNameRegistrationErrorReturn':hm2TrackingTrackNameRegistrationErrorReturn,'hm2TrackingTrackNameDeregisterationErrorReturn':hm2TrackingTrackNameDeregisterationErrorReturn,'hm2TrackingInterfaceStatusGroup':hm2TrackingInterfaceStatusGroup,'hm2TrackInterfaceStatusTable':hm2TrackInterfaceStatusTable,_V:hm2TrackInterfaceStatusEntry,'hm2TrackInterfaceStatusTrackId':hm2TrackInterfaceStatusTrackId,'hm2TrackInterfaceStatusTrackState':hm2TrackInterfaceStatusTrackState})