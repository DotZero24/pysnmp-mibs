_V='extremeMacTrackingPrevPortIfIndex'
_U='extremeFdbMacFdbCounterPortIfIndex'
_T='extremeFdbMacExosFdbVlanIfIndex'
_S='extremeFdbMacExosFdbMacAddress'
_R='extremeFdbPermFdbVlanId'
_Q='extremeFdbPermFdbMacAddress'
_P='extremeFdbPermFdbFilterNum'
_O='extremeFdbIpFdbSequenceNumber'
_N='learned'
_M='invalid'
_L='extremeFdbMacFdbSequenceNumber'
_K='extremeFdbMacFdbVlanIfIndex'
_J='read-create'
_I='Integer32'
_H='extremeMacTrackingPortIfIndex'
_G='extremeMacTrackingVlanIfIndex'
_F='extremeMacTrackingMacAddress'
_E='accessible-for-notify'
_D='not-accessible'
_C='read-only'
_B='EXTREME-FDB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
extremeFdb=ModuleIdentity((1,3,6,1,4,1,1916,1,16))
_ExtremeFdbMacFdbTable_Object=MibTable
extremeFdbMacFdbTable=_ExtremeFdbMacFdbTable_Object((1,3,6,1,4,1,1916,1,16,1))
if mibBuilder.loadTexts:extremeFdbMacFdbTable.setStatus(_A)
_ExtremeFdbMacFdbEntry_Object=MibTableRow
extremeFdbMacFdbEntry=_ExtremeFdbMacFdbEntry_Object((1,3,6,1,4,1,1916,1,16,1,1))
extremeFdbMacFdbEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:extremeFdbMacFdbEntry.setStatus(_A)
_ExtremeFdbMacFdbVlanIfIndex_Type=Integer32
_ExtremeFdbMacFdbVlanIfIndex_Object=MibTableColumn
extremeFdbMacFdbVlanIfIndex=_ExtremeFdbMacFdbVlanIfIndex_Object((1,3,6,1,4,1,1916,1,16,1,1,1),_ExtremeFdbMacFdbVlanIfIndex_Type())
extremeFdbMacFdbVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFdbMacFdbVlanIfIndex.setStatus(_A)
_ExtremeFdbMacFdbSequenceNumber_Type=Integer32
_ExtremeFdbMacFdbSequenceNumber_Object=MibTableColumn
extremeFdbMacFdbSequenceNumber=_ExtremeFdbMacFdbSequenceNumber_Object((1,3,6,1,4,1,1916,1,16,1,1,2),_ExtremeFdbMacFdbSequenceNumber_Type())
extremeFdbMacFdbSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFdbMacFdbSequenceNumber.setStatus(_A)
_ExtremeFdbMacFdbMacAddress_Type=MacAddress
_ExtremeFdbMacFdbMacAddress_Object=MibTableColumn
extremeFdbMacFdbMacAddress=_ExtremeFdbMacFdbMacAddress_Object((1,3,6,1,4,1,1916,1,16,1,1,3),_ExtremeFdbMacFdbMacAddress_Type())
extremeFdbMacFdbMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacFdbMacAddress.setStatus(_A)
_ExtremeFdbMacFdbPortIfIndex_Type=Integer32
_ExtremeFdbMacFdbPortIfIndex_Object=MibTableColumn
extremeFdbMacFdbPortIfIndex=_ExtremeFdbMacFdbPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,1,1,4),_ExtremeFdbMacFdbPortIfIndex_Type())
extremeFdbMacFdbPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacFdbPortIfIndex.setStatus(_A)
class _ExtremeFdbMacFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_M,2),(_N,3),('self',4),('mgmt',5)))
_ExtremeFdbMacFdbStatus_Type.__name__=_I
_ExtremeFdbMacFdbStatus_Object=MibTableColumn
extremeFdbMacFdbStatus=_ExtremeFdbMacFdbStatus_Object((1,3,6,1,4,1,1916,1,16,1,1,5),_ExtremeFdbMacFdbStatus_Type())
extremeFdbMacFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacFdbStatus.setStatus(_A)
_ExtremeFdbIpFdbTable_Object=MibTable
extremeFdbIpFdbTable=_ExtremeFdbIpFdbTable_Object((1,3,6,1,4,1,1916,1,16,2))
if mibBuilder.loadTexts:extremeFdbIpFdbTable.setStatus(_A)
_ExtremeFdbIpFdbEntry_Object=MibTableRow
extremeFdbIpFdbEntry=_ExtremeFdbIpFdbEntry_Object((1,3,6,1,4,1,1916,1,16,2,1))
extremeFdbIpFdbEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:extremeFdbIpFdbEntry.setStatus(_A)
_ExtremeFdbIpFdbSequenceNumber_Type=Integer32
_ExtremeFdbIpFdbSequenceNumber_Object=MibTableColumn
extremeFdbIpFdbSequenceNumber=_ExtremeFdbIpFdbSequenceNumber_Object((1,3,6,1,4,1,1916,1,16,2,1,1),_ExtremeFdbIpFdbSequenceNumber_Type())
extremeFdbIpFdbSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFdbIpFdbSequenceNumber.setStatus(_A)
_ExtremeFdbIpFdbIPAddress_Type=IpAddress
_ExtremeFdbIpFdbIPAddress_Object=MibTableColumn
extremeFdbIpFdbIPAddress=_ExtremeFdbIpFdbIPAddress_Object((1,3,6,1,4,1,1916,1,16,2,1,2),_ExtremeFdbIpFdbIPAddress_Type())
extremeFdbIpFdbIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbIpFdbIPAddress.setStatus(_A)
_ExtremeFdbIpFdbMacAddress_Type=MacAddress
_ExtremeFdbIpFdbMacAddress_Object=MibTableColumn
extremeFdbIpFdbMacAddress=_ExtremeFdbIpFdbMacAddress_Object((1,3,6,1,4,1,1916,1,16,2,1,3),_ExtremeFdbIpFdbMacAddress_Type())
extremeFdbIpFdbMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbIpFdbMacAddress.setStatus(_A)
_ExtremeFdbIpFdbVlanIfIndex_Type=Integer32
_ExtremeFdbIpFdbVlanIfIndex_Object=MibTableColumn
extremeFdbIpFdbVlanIfIndex=_ExtremeFdbIpFdbVlanIfIndex_Object((1,3,6,1,4,1,1916,1,16,2,1,4),_ExtremeFdbIpFdbVlanIfIndex_Type())
extremeFdbIpFdbVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbIpFdbVlanIfIndex.setStatus(_A)
_ExtremeFdbIpFdbPortIfIndex_Type=Integer32
_ExtremeFdbIpFdbPortIfIndex_Object=MibTableColumn
extremeFdbIpFdbPortIfIndex=_ExtremeFdbIpFdbPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,2,1,5),_ExtremeFdbIpFdbPortIfIndex_Type())
extremeFdbIpFdbPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbIpFdbPortIfIndex.setStatus(_A)
_ExtremeFdbPermFdbTable_Object=MibTable
extremeFdbPermFdbTable=_ExtremeFdbPermFdbTable_Object((1,3,6,1,4,1,1916,1,16,3))
if mibBuilder.loadTexts:extremeFdbPermFdbTable.setStatus(_A)
_ExtremeFdbPermFdbEntry_Object=MibTableRow
extremeFdbPermFdbEntry=_ExtremeFdbPermFdbEntry_Object((1,3,6,1,4,1,1916,1,16,3,1))
extremeFdbPermFdbEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:extremeFdbPermFdbEntry.setStatus(_A)
_ExtremeFdbPermFdbFilterNum_Type=Integer32
_ExtremeFdbPermFdbFilterNum_Object=MibTableColumn
extremeFdbPermFdbFilterNum=_ExtremeFdbPermFdbFilterNum_Object((1,3,6,1,4,1,1916,1,16,3,1,1),_ExtremeFdbPermFdbFilterNum_Type())
extremeFdbPermFdbFilterNum.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbPermFdbFilterNum.setStatus(_A)
_ExtremeFdbPermFdbMacAddress_Type=MacAddress
_ExtremeFdbPermFdbMacAddress_Object=MibTableColumn
extremeFdbPermFdbMacAddress=_ExtremeFdbPermFdbMacAddress_Object((1,3,6,1,4,1,1916,1,16,3,1,2),_ExtremeFdbPermFdbMacAddress_Type())
extremeFdbPermFdbMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbPermFdbMacAddress.setStatus(_A)
_ExtremeFdbPermFdbVlanId_Type=Integer32
_ExtremeFdbPermFdbVlanId_Object=MibTableColumn
extremeFdbPermFdbVlanId=_ExtremeFdbPermFdbVlanId_Object((1,3,6,1,4,1,1916,1,16,3,1,3),_ExtremeFdbPermFdbVlanId_Type())
extremeFdbPermFdbVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbPermFdbVlanId.setStatus(_A)
_ExtremeFdbPermFdbPortList_Type=PortList
_ExtremeFdbPermFdbPortList_Object=MibTableColumn
extremeFdbPermFdbPortList=_ExtremeFdbPermFdbPortList_Object((1,3,6,1,4,1,1916,1,16,3,1,4),_ExtremeFdbPermFdbPortList_Type())
extremeFdbPermFdbPortList.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeFdbPermFdbPortList.setStatus(_A)
class _ExtremeFdbPermFdbFlags_Type(Bits):namedValues=NamedValues(('isSecure',0))
_ExtremeFdbPermFdbFlags_Type.__name__='Bits'
_ExtremeFdbPermFdbFlags_Object=MibTableColumn
extremeFdbPermFdbFlags=_ExtremeFdbPermFdbFlags_Object((1,3,6,1,4,1,1916,1,16,3,1,5),_ExtremeFdbPermFdbFlags_Type())
extremeFdbPermFdbFlags.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeFdbPermFdbFlags.setStatus(_A)
_ExtremeFdbPermFdbStatus_Type=RowStatus
_ExtremeFdbPermFdbStatus_Object=MibTableColumn
extremeFdbPermFdbStatus=_ExtremeFdbPermFdbStatus_Object((1,3,6,1,4,1,1916,1,16,3,1,6),_ExtremeFdbPermFdbStatus_Type())
extremeFdbPermFdbStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeFdbPermFdbStatus.setStatus(_A)
_ExtremeFdbMacExosFdbTable_Object=MibTable
extremeFdbMacExosFdbTable=_ExtremeFdbMacExosFdbTable_Object((1,3,6,1,4,1,1916,1,16,4))
if mibBuilder.loadTexts:extremeFdbMacExosFdbTable.setStatus(_A)
_ExtremeFdbMacExosFdbEntry_Object=MibTableRow
extremeFdbMacExosFdbEntry=_ExtremeFdbMacExosFdbEntry_Object((1,3,6,1,4,1,1916,1,16,4,1))
extremeFdbMacExosFdbEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:extremeFdbMacExosFdbEntry.setStatus(_A)
_ExtremeFdbMacExosFdbMacAddress_Type=MacAddress
_ExtremeFdbMacExosFdbMacAddress_Object=MibTableColumn
extremeFdbMacExosFdbMacAddress=_ExtremeFdbMacExosFdbMacAddress_Object((1,3,6,1,4,1,1916,1,16,4,1,1),_ExtremeFdbMacExosFdbMacAddress_Type())
extremeFdbMacExosFdbMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacExosFdbMacAddress.setStatus(_A)
_ExtremeFdbMacExosFdbVlanIfIndex_Type=Integer32
_ExtremeFdbMacExosFdbVlanIfIndex_Object=MibTableColumn
extremeFdbMacExosFdbVlanIfIndex=_ExtremeFdbMacExosFdbVlanIfIndex_Object((1,3,6,1,4,1,1916,1,16,4,1,2),_ExtremeFdbMacExosFdbVlanIfIndex_Type())
extremeFdbMacExosFdbVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacExosFdbVlanIfIndex.setStatus(_A)
_ExtremeFdbMacExosFdbPortIfIndex_Type=Integer32
_ExtremeFdbMacExosFdbPortIfIndex_Object=MibTableColumn
extremeFdbMacExosFdbPortIfIndex=_ExtremeFdbMacExosFdbPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,4,1,3),_ExtremeFdbMacExosFdbPortIfIndex_Type())
extremeFdbMacExosFdbPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacExosFdbPortIfIndex.setStatus(_A)
class _ExtremeFdbMacExosFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_M,2),(_N,3),('self',4),('mgmt',5)))
_ExtremeFdbMacExosFdbStatus_Type.__name__=_I
_ExtremeFdbMacExosFdbStatus_Object=MibTableColumn
extremeFdbMacExosFdbStatus=_ExtremeFdbMacExosFdbStatus_Object((1,3,6,1,4,1,1916,1,16,4,1,4),_ExtremeFdbMacExosFdbStatus_Type())
extremeFdbMacExosFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacExosFdbStatus.setStatus(_A)
_ExtremeFdbMacFdbCounterTable_Object=MibTable
extremeFdbMacFdbCounterTable=_ExtremeFdbMacFdbCounterTable_Object((1,3,6,1,4,1,1916,1,16,5))
if mibBuilder.loadTexts:extremeFdbMacFdbCounterTable.setStatus(_A)
_ExtremeFdbMacFdbCounterEntry_Object=MibTableRow
extremeFdbMacFdbCounterEntry=_ExtremeFdbMacFdbCounterEntry_Object((1,3,6,1,4,1,1916,1,16,5,1))
extremeFdbMacFdbCounterEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:extremeFdbMacFdbCounterEntry.setStatus(_A)
_ExtremeFdbMacFdbCounterPortIfIndex_Type=Integer32
_ExtremeFdbMacFdbCounterPortIfIndex_Object=MibTableColumn
extremeFdbMacFdbCounterPortIfIndex=_ExtremeFdbMacFdbCounterPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,5,1,1),_ExtremeFdbMacFdbCounterPortIfIndex_Type())
extremeFdbMacFdbCounterPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFdbMacFdbCounterPortIfIndex.setStatus(_A)
_ExtremeFdbMacFdbCounterValue_Type=Counter64
_ExtremeFdbMacFdbCounterValue_Object=MibTableColumn
extremeFdbMacFdbCounterValue=_ExtremeFdbMacFdbCounterValue_Object((1,3,6,1,4,1,1916,1,16,5,1,2),_ExtremeFdbMacFdbCounterValue_Type())
extremeFdbMacFdbCounterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeFdbMacFdbCounterValue.setStatus(_A)
_ExtremeMacTrackingTraps_ObjectIdentity=ObjectIdentity
extremeMacTrackingTraps=_ExtremeMacTrackingTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,16,6))
_ExtremeMacTrackingTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeMacTrackingTrapsPrefix=_ExtremeMacTrackingTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,16,6,0))
_ExtremeMacTrackingMacAddress_Type=MacAddress
_ExtremeMacTrackingMacAddress_Object=MibScalar
extremeMacTrackingMacAddress=_ExtremeMacTrackingMacAddress_Object((1,3,6,1,4,1,1916,1,16,6,1),_ExtremeMacTrackingMacAddress_Type())
extremeMacTrackingMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeMacTrackingMacAddress.setStatus(_A)
_ExtremeMacTrackingPortIfIndex_Type=Integer32
_ExtremeMacTrackingPortIfIndex_Object=MibScalar
extremeMacTrackingPortIfIndex=_ExtremeMacTrackingPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,6,2),_ExtremeMacTrackingPortIfIndex_Type())
extremeMacTrackingPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeMacTrackingPortIfIndex.setStatus(_A)
_ExtremeMacTrackingPrevPortIfIndex_Type=Integer32
_ExtremeMacTrackingPrevPortIfIndex_Object=MibScalar
extremeMacTrackingPrevPortIfIndex=_ExtremeMacTrackingPrevPortIfIndex_Object((1,3,6,1,4,1,1916,1,16,6,3),_ExtremeMacTrackingPrevPortIfIndex_Type())
extremeMacTrackingPrevPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeMacTrackingPrevPortIfIndex.setStatus(_A)
_ExtremeMacTrackingVlanIfIndex_Type=Integer32
_ExtremeMacTrackingVlanIfIndex_Object=MibScalar
extremeMacTrackingVlanIfIndex=_ExtremeMacTrackingVlanIfIndex_Object((1,3,6,1,4,1,1916,1,16,6,4),_ExtremeMacTrackingVlanIfIndex_Type())
extremeMacTrackingVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeMacTrackingVlanIfIndex.setStatus(_A)
extremeMACTrackingAdd=NotificationType((1,3,6,1,4,1,1916,1,16,6,0,1))
extremeMACTrackingAdd.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:extremeMACTrackingAdd.setStatus(_A)
extremeMACTrackingDel=NotificationType((1,3,6,1,4,1,1916,1,16,6,0,2))
extremeMACTrackingDel.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:extremeMACTrackingDel.setStatus(_A)
extremeMACTrackingMove=NotificationType((1,3,6,1,4,1,1916,1,16,6,0,3))
extremeMACTrackingMove.setObjects(*((_B,_F),(_B,_G),(_B,_V),(_B,_H)))
if mibBuilder.loadTexts:extremeMACTrackingMove.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeFdb':extremeFdb,'extremeFdbMacFdbTable':extremeFdbMacFdbTable,'extremeFdbMacFdbEntry':extremeFdbMacFdbEntry,_K:extremeFdbMacFdbVlanIfIndex,_L:extremeFdbMacFdbSequenceNumber,'extremeFdbMacFdbMacAddress':extremeFdbMacFdbMacAddress,'extremeFdbMacFdbPortIfIndex':extremeFdbMacFdbPortIfIndex,'extremeFdbMacFdbStatus':extremeFdbMacFdbStatus,'extremeFdbIpFdbTable':extremeFdbIpFdbTable,'extremeFdbIpFdbEntry':extremeFdbIpFdbEntry,_O:extremeFdbIpFdbSequenceNumber,'extremeFdbIpFdbIPAddress':extremeFdbIpFdbIPAddress,'extremeFdbIpFdbMacAddress':extremeFdbIpFdbMacAddress,'extremeFdbIpFdbVlanIfIndex':extremeFdbIpFdbVlanIfIndex,'extremeFdbIpFdbPortIfIndex':extremeFdbIpFdbPortIfIndex,'extremeFdbPermFdbTable':extremeFdbPermFdbTable,'extremeFdbPermFdbEntry':extremeFdbPermFdbEntry,_P:extremeFdbPermFdbFilterNum,_Q:extremeFdbPermFdbMacAddress,_R:extremeFdbPermFdbVlanId,'extremeFdbPermFdbPortList':extremeFdbPermFdbPortList,'extremeFdbPermFdbFlags':extremeFdbPermFdbFlags,'extremeFdbPermFdbStatus':extremeFdbPermFdbStatus,'extremeFdbMacExosFdbTable':extremeFdbMacExosFdbTable,'extremeFdbMacExosFdbEntry':extremeFdbMacExosFdbEntry,_S:extremeFdbMacExosFdbMacAddress,_T:extremeFdbMacExosFdbVlanIfIndex,'extremeFdbMacExosFdbPortIfIndex':extremeFdbMacExosFdbPortIfIndex,'extremeFdbMacExosFdbStatus':extremeFdbMacExosFdbStatus,'extremeFdbMacFdbCounterTable':extremeFdbMacFdbCounterTable,'extremeFdbMacFdbCounterEntry':extremeFdbMacFdbCounterEntry,_U:extremeFdbMacFdbCounterPortIfIndex,'extremeFdbMacFdbCounterValue':extremeFdbMacFdbCounterValue,'extremeMacTrackingTraps':extremeMacTrackingTraps,'extremeMacTrackingTrapsPrefix':extremeMacTrackingTrapsPrefix,'extremeMACTrackingAdd':extremeMACTrackingAdd,'extremeMACTrackingDel':extremeMACTrackingDel,'extremeMACTrackingMove':extremeMACTrackingMove,_F:extremeMacTrackingMacAddress,_H:extremeMacTrackingPortIfIndex,_V:extremeMacTrackingPrevPortIfIndex,_G:extremeMacTrackingVlanIfIndex})