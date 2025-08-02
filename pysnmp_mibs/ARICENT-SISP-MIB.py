_J='fsSispCxtClassificationVlanId'
_I='read-only'
_H='read-create'
_G='fsSispPortMapContextId'
_F='read-write'
_E='not-accessible'
_D='fsSispPortIndex'
_C='Integer32'
_B='ARICENT-SISP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('ARICENTQ-BRIDGE-MIB','VlanId')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fssisp=ModuleIdentity((1,3,6,1,4,1,29601,2,20))
if mibBuilder.loadTexts:fssisp.setRevisions(('2012-09-05 00:00',))
_FsSispSystemGroup_ObjectIdentity=ObjectIdentity
fsSispSystemGroup=_FsSispSystemGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,20,1))
class _FsSispSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsSispSystemControl_Type.__name__=_C
_FsSispSystemControl_Object=MibScalar
fsSispSystemControl=_FsSispSystemControl_Object((1,3,6,1,4,1,29601,2,20,1,1),_FsSispSystemControl_Type())
fsSispSystemControl.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSispSystemControl.setStatus(_A)
_FsSispConfig_ObjectIdentity=ObjectIdentity
fsSispConfig=_FsSispConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,20,2))
_FsSispPortTable_Object=MibTable
fsSispPortTable=_FsSispPortTable_Object((1,3,6,1,4,1,29601,2,20,2,1))
if mibBuilder.loadTexts:fsSispPortTable.setStatus(_A)
_FsSispPortEntry_Object=MibTableRow
fsSispPortEntry=_FsSispPortEntry_Object((1,3,6,1,4,1,29601,2,20,2,1,1))
fsSispPortEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsSispPortEntry.setStatus(_A)
_FsSispPortIndex_Type=InterfaceIndex
_FsSispPortIndex_Object=MibTableColumn
fsSispPortIndex=_FsSispPortIndex_Object((1,3,6,1,4,1,29601,2,20,2,1,1,1),_FsSispPortIndex_Type())
fsSispPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSispPortIndex.setStatus(_A)
class _FsSispPortCtrlStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsSispPortCtrlStatus_Type.__name__=_C
_FsSispPortCtrlStatus_Object=MibTableColumn
fsSispPortCtrlStatus=_FsSispPortCtrlStatus_Object((1,3,6,1,4,1,29601,2,20,2,1,1,2),_FsSispPortCtrlStatus_Type())
fsSispPortCtrlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSispPortCtrlStatus.setStatus(_A)
_FsSispPortMapTable_Object=MibTable
fsSispPortMapTable=_FsSispPortMapTable_Object((1,3,6,1,4,1,29601,2,20,2,2))
if mibBuilder.loadTexts:fsSispPortMapTable.setStatus(_A)
_FsSispPortMapEntry_Object=MibTableRow
fsSispPortMapEntry=_FsSispPortMapEntry_Object((1,3,6,1,4,1,29601,2,20,2,2,1))
fsSispPortMapEntry.setIndexNames((0,_B,_D),(0,_B,_G))
if mibBuilder.loadTexts:fsSispPortMapEntry.setStatus(_A)
class _FsSispPortMapContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSispPortMapContextId_Type.__name__=_C
_FsSispPortMapContextId_Object=MibTableColumn
fsSispPortMapContextId=_FsSispPortMapContextId_Object((1,3,6,1,4,1,29601,2,20,2,2,1,1),_FsSispPortMapContextId_Type())
fsSispPortMapContextId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSispPortMapContextId.setStatus(_A)
_FsSispPortMapSharedPort_Type=InterfaceIndex
_FsSispPortMapSharedPort_Object=MibTableColumn
fsSispPortMapSharedPort=_FsSispPortMapSharedPort_Object((1,3,6,1,4,1,29601,2,20,2,2,1,2),_FsSispPortMapSharedPort_Type())
fsSispPortMapSharedPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSispPortMapSharedPort.setStatus(_A)
_FsSispPortMapHlPortId_Type=InterfaceIndexOrZero
_FsSispPortMapHlPortId_Object=MibTableColumn
fsSispPortMapHlPortId=_FsSispPortMapHlPortId_Object((1,3,6,1,4,1,29601,2,20,2,2,1,3),_FsSispPortMapHlPortId_Type())
fsSispPortMapHlPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsSispPortMapHlPortId.setStatus(_A)
_FsSispPortMapRowStatus_Type=RowStatus
_FsSispPortMapRowStatus_Object=MibTableColumn
fsSispPortMapRowStatus=_FsSispPortMapRowStatus_Object((1,3,6,1,4,1,29601,2,20,2,2,1,4),_FsSispPortMapRowStatus_Type())
fsSispPortMapRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsSispPortMapRowStatus.setStatus(_A)
_FsSispInfo_ObjectIdentity=ObjectIdentity
fsSispInfo=_FsSispInfo_ObjectIdentity((1,3,6,1,4,1,29601,2,20,3))
_FsSispCxtClassificationTable_Object=MibTable
fsSispCxtClassificationTable=_FsSispCxtClassificationTable_Object((1,3,6,1,4,1,29601,2,20,3,1))
if mibBuilder.loadTexts:fsSispCxtClassificationTable.setStatus(_A)
_FsSispCxtClassificationEntry_Object=MibTableRow
fsSispCxtClassificationEntry=_FsSispCxtClassificationEntry_Object((1,3,6,1,4,1,29601,2,20,3,1,1))
fsSispCxtClassificationEntry.setIndexNames((0,_B,_D),(0,_B,_J))
if mibBuilder.loadTexts:fsSispCxtClassificationEntry.setStatus(_A)
_FsSispCxtClassificationVlanId_Type=VlanId
_FsSispCxtClassificationVlanId_Object=MibTableColumn
fsSispCxtClassificationVlanId=_FsSispCxtClassificationVlanId_Object((1,3,6,1,4,1,29601,2,20,3,1,1,1),_FsSispCxtClassificationVlanId_Type())
fsSispCxtClassificationVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSispCxtClassificationVlanId.setStatus(_A)
class _FsSispCxtClassificationCxtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSispCxtClassificationCxtId_Type.__name__=_C
_FsSispCxtClassificationCxtId_Object=MibTableColumn
fsSispCxtClassificationCxtId=_FsSispCxtClassificationCxtId_Object((1,3,6,1,4,1,29601,2,20,3,1,1,2),_FsSispCxtClassificationCxtId_Type())
fsSispCxtClassificationCxtId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsSispCxtClassificationCxtId.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fssisp':fssisp,'fsSispSystemGroup':fsSispSystemGroup,'fsSispSystemControl':fsSispSystemControl,'fsSispConfig':fsSispConfig,'fsSispPortTable':fsSispPortTable,'fsSispPortEntry':fsSispPortEntry,_D:fsSispPortIndex,'fsSispPortCtrlStatus':fsSispPortCtrlStatus,'fsSispPortMapTable':fsSispPortMapTable,'fsSispPortMapEntry':fsSispPortMapEntry,_G:fsSispPortMapContextId,'fsSispPortMapSharedPort':fsSispPortMapSharedPort,'fsSispPortMapHlPortId':fsSispPortMapHlPortId,'fsSispPortMapRowStatus':fsSispPortMapRowStatus,'fsSispInfo':fsSispInfo,'fsSispCxtClassificationTable':fsSispCxtClassificationTable,'fsSispCxtClassificationEntry':fsSispCxtClassificationEntry,_J:fsSispCxtClassificationVlanId,'fsSispCxtClassificationCxtId':fsSispCxtClassificationCxtId})