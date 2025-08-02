_P='hpnicfFcTraceRouteOperStatus'
_O='hpnicfFcTraceRouteAddress'
_N='hpnicfFcTraceRouteAddressType'
_M='hpnicfFcTraceRouteVsan'
_L='hpnicfFcTraceRouteHopsIndex'
_K='read-only'
_J='seconds'
_I='TruthValue'
_H='Integer32'
_G='HpnicfFcStartOper'
_F='HpnicfFcAddressType'
_E='hpnicfFcTraceRouteIndex'
_D='Unsigned32'
_C='read-create'
_B='HPN-ICF-FC-TRACE-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcAddress,HpnicfFcAddressType,HpnicfFcNameId,HpnicfFcStartOper,HpnicfFcVsanIndex=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcAddress',_F,'HpnicfFcNameId',_G,'HpnicfFcVsanIndex')
hpnicfSan,=mibBuilder.importSymbols('HPN-ICF-VSAN-MIB','hpnicfSan')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfFcTraceRoute=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4))
if mibBuilder.loadTexts:hpnicfFcTraceRoute.setRevisions(('2013-02-27 00:00',))
_HpnicfFcTraceRouteObjects_ObjectIdentity=ObjectIdentity
hpnicfFcTraceRouteObjects=_HpnicfFcTraceRouteObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1))
_HpnicfFcTraceRouteConfigurations_ObjectIdentity=ObjectIdentity
hpnicfFcTraceRouteConfigurations=_HpnicfFcTraceRouteConfigurations_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1))
_HpnicfFcTraceRouteTable_Object=MibTable
hpnicfFcTraceRouteTable=_HpnicfFcTraceRouteTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1))
if mibBuilder.loadTexts:hpnicfFcTraceRouteTable.setStatus(_A)
_HpnicfFcTraceRouteEntry_Object=MibTableRow
hpnicfFcTraceRouteEntry=_HpnicfFcTraceRouteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1))
hpnicfFcTraceRouteEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfFcTraceRouteEntry.setStatus(_A)
class _HpnicfFcTraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfFcTraceRouteIndex_Type.__name__=_D
_HpnicfFcTraceRouteIndex_Object=MibTableColumn
hpnicfFcTraceRouteIndex=_HpnicfFcTraceRouteIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,1),_HpnicfFcTraceRouteIndex_Type())
hpnicfFcTraceRouteIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfFcTraceRouteIndex.setStatus(_A)
_HpnicfFcTraceRouteVsan_Type=HpnicfFcVsanIndex
_HpnicfFcTraceRouteVsan_Object=MibTableColumn
hpnicfFcTraceRouteVsan=_HpnicfFcTraceRouteVsan_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,2),_HpnicfFcTraceRouteVsan_Type())
hpnicfFcTraceRouteVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteVsan.setStatus(_A)
class _HpnicfFcTraceRouteAddressType_Type(HpnicfFcAddressType):defaultValue=2
_HpnicfFcTraceRouteAddressType_Type.__name__=_F
_HpnicfFcTraceRouteAddressType_Object=MibTableColumn
hpnicfFcTraceRouteAddressType=_HpnicfFcTraceRouteAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,3),_HpnicfFcTraceRouteAddressType_Type())
hpnicfFcTraceRouteAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteAddressType.setStatus(_A)
_HpnicfFcTraceRouteAddress_Type=HpnicfFcAddress
_HpnicfFcTraceRouteAddress_Object=MibTableColumn
hpnicfFcTraceRouteAddress=_HpnicfFcTraceRouteAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,4),_HpnicfFcTraceRouteAddress_Type())
hpnicfFcTraceRouteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteAddress.setStatus(_A)
class _HpnicfFcTraceRouteTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfFcTraceRouteTimeout_Type.__name__=_D
_HpnicfFcTraceRouteTimeout_Object=MibTableColumn
hpnicfFcTraceRouteTimeout=_HpnicfFcTraceRouteTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,5),_HpnicfFcTraceRouteTimeout_Type())
hpnicfFcTraceRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcTraceRouteTimeout.setUnits(_J)
class _HpnicfFcTraceRouteAdminStatus_Type(HpnicfFcStartOper):defaultValue=2
_HpnicfFcTraceRouteAdminStatus_Type.__name__=_G
_HpnicfFcTraceRouteAdminStatus_Object=MibTableColumn
hpnicfFcTraceRouteAdminStatus=_HpnicfFcTraceRouteAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,6),_HpnicfFcTraceRouteAdminStatus_Type())
hpnicfFcTraceRouteAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteAdminStatus.setStatus(_A)
class _HpnicfFcTraceRouteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inProgress',1),('success',2),('partialSuccess',3),('failure',4),('disabled',5)))
_HpnicfFcTraceRouteOperStatus_Type.__name__=_H
_HpnicfFcTraceRouteOperStatus_Object=MibTableColumn
hpnicfFcTraceRouteOperStatus=_HpnicfFcTraceRouteOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,7),_HpnicfFcTraceRouteOperStatus_Type())
hpnicfFcTraceRouteOperStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcTraceRouteOperStatus.setStatus(_A)
class _HpnicfFcTraceRouteAgeInterval_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,900))
_HpnicfFcTraceRouteAgeInterval_Type.__name__=_D
_HpnicfFcTraceRouteAgeInterval_Object=MibTableColumn
hpnicfFcTraceRouteAgeInterval=_HpnicfFcTraceRouteAgeInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,8),_HpnicfFcTraceRouteAgeInterval_Type())
hpnicfFcTraceRouteAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcTraceRouteAgeInterval.setUnits(_J)
class _HpnicfFcTraceRouteTrapOnCompletion_Type(TruthValue):defaultValue=2
_HpnicfFcTraceRouteTrapOnCompletion_Type.__name__=_I
_HpnicfFcTraceRouteTrapOnCompletion_Object=MibTableColumn
hpnicfFcTraceRouteTrapOnCompletion=_HpnicfFcTraceRouteTrapOnCompletion_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,9),_HpnicfFcTraceRouteTrapOnCompletion_Type())
hpnicfFcTraceRouteTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteTrapOnCompletion.setStatus(_A)
_HpnicfFcTraceRouteRowStatus_Type=RowStatus
_HpnicfFcTraceRouteRowStatus_Object=MibTableColumn
hpnicfFcTraceRouteRowStatus=_HpnicfFcTraceRouteRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,1,1,1,10),_HpnicfFcTraceRouteRowStatus_Type())
hpnicfFcTraceRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcTraceRouteRowStatus.setStatus(_A)
_HpnicfFcTraceRouteResults_ObjectIdentity=ObjectIdentity
hpnicfFcTraceRouteResults=_HpnicfFcTraceRouteResults_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,2))
_HpnicfFcTraceRouteHopsTable_Object=MibTable
hpnicfFcTraceRouteHopsTable=_HpnicfFcTraceRouteHopsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,2,1))
if mibBuilder.loadTexts:hpnicfFcTraceRouteHopsTable.setStatus(_A)
_HpnicfFcTraceRouteHopsEntry_Object=MibTableRow
hpnicfFcTraceRouteHopsEntry=_HpnicfFcTraceRouteHopsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,2,1,1))
hpnicfFcTraceRouteHopsEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfFcTraceRouteHopsEntry.setStatus(_A)
class _HpnicfFcTraceRouteHopsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfFcTraceRouteHopsIndex_Type.__name__=_D
_HpnicfFcTraceRouteHopsIndex_Object=MibTableColumn
hpnicfFcTraceRouteHopsIndex=_HpnicfFcTraceRouteHopsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,2,1,1,1),_HpnicfFcTraceRouteHopsIndex_Type())
hpnicfFcTraceRouteHopsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfFcTraceRouteHopsIndex.setStatus(_A)
_HpnicfFcTraceRouteHopsAddr_Type=HpnicfFcNameId
_HpnicfFcTraceRouteHopsAddr_Object=MibTableColumn
hpnicfFcTraceRouteHopsAddr=_HpnicfFcTraceRouteHopsAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,2,1,1,2),_HpnicfFcTraceRouteHopsAddr_Type())
hpnicfFcTraceRouteHopsAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcTraceRouteHopsAddr.setStatus(_A)
_HpnicfFcTraceRouteNotifications_ObjectIdentity=ObjectIdentity
hpnicfFcTraceRouteNotifications=_HpnicfFcTraceRouteNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,3))
_HpnicfFcTraceRouteNotifyPrefix_ObjectIdentity=ObjectIdentity
hpnicfFcTraceRouteNotifyPrefix=_HpnicfFcTraceRouteNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,3,0))
hpnicfFcTraceRouteCompletionNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,4,1,3,0,1))
hpnicfFcTraceRouteCompletionNotify.setObjects(*((_B,_E),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpnicfFcTraceRouteCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfFcTraceRoute':hpnicfFcTraceRoute,'hpnicfFcTraceRouteObjects':hpnicfFcTraceRouteObjects,'hpnicfFcTraceRouteConfigurations':hpnicfFcTraceRouteConfigurations,'hpnicfFcTraceRouteTable':hpnicfFcTraceRouteTable,'hpnicfFcTraceRouteEntry':hpnicfFcTraceRouteEntry,_E:hpnicfFcTraceRouteIndex,_M:hpnicfFcTraceRouteVsan,_N:hpnicfFcTraceRouteAddressType,_O:hpnicfFcTraceRouteAddress,'hpnicfFcTraceRouteTimeout':hpnicfFcTraceRouteTimeout,'hpnicfFcTraceRouteAdminStatus':hpnicfFcTraceRouteAdminStatus,_P:hpnicfFcTraceRouteOperStatus,'hpnicfFcTraceRouteAgeInterval':hpnicfFcTraceRouteAgeInterval,'hpnicfFcTraceRouteTrapOnCompletion':hpnicfFcTraceRouteTrapOnCompletion,'hpnicfFcTraceRouteRowStatus':hpnicfFcTraceRouteRowStatus,'hpnicfFcTraceRouteResults':hpnicfFcTraceRouteResults,'hpnicfFcTraceRouteHopsTable':hpnicfFcTraceRouteHopsTable,'hpnicfFcTraceRouteHopsEntry':hpnicfFcTraceRouteHopsEntry,_L:hpnicfFcTraceRouteHopsIndex,'hpnicfFcTraceRouteHopsAddr':hpnicfFcTraceRouteHopsAddr,'hpnicfFcTraceRouteNotifications':hpnicfFcTraceRouteNotifications,'hpnicfFcTraceRouteNotifyPrefix':hpnicfFcTraceRouteNotifyPrefix,'hpnicfFcTraceRouteCompletionNotify':hpnicfFcTraceRouteCompletionNotify})