_G='read-only'
_F='wfDot1qTagCfgLocalVlanId'
_E='wfDot1qTagCfgPhysicalPortId'
_D='Wellfleet-DOT1QTAG-CONFIG-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wfDot1qTagConfigGroup,=mibBuilder.importSymbols('Wellfleet-COMMON-MIB','wfDot1qTagConfigGroup')
_WfDot1qTagConfig_ObjectIdentity=ObjectIdentity
wfDot1qTagConfig=_WfDot1qTagConfig_ObjectIdentity((1,3,6,1,4,1,18,3,5,1,12,6,1))
_WfDot1qTagConfigTable_Object=MibTable
wfDot1qTagConfigTable=_WfDot1qTagConfigTable_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1))
if mibBuilder.loadTexts:wfDot1qTagConfigTable.setStatus(_A)
_WfDot1qTagConfigEntry_Object=MibTableRow
wfDot1qTagConfigEntry=_WfDot1qTagConfigEntry_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1))
wfDot1qTagConfigEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:wfDot1qTagConfigEntry.setStatus(_A)
class _WfDot1qTagCfgDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('create',1),('delete',2)))
_WfDot1qTagCfgDelete_Type.__name__=_B
_WfDot1qTagCfgDelete_Object=MibTableColumn
wfDot1qTagCfgDelete=_WfDot1qTagCfgDelete_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,1),_WfDot1qTagCfgDelete_Type())
wfDot1qTagCfgDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgDelete.setStatus(_A)
class _WfDot1qTagCfgDisable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_WfDot1qTagCfgDisable_Type.__name__=_B
_WfDot1qTagCfgDisable_Object=MibTableColumn
wfDot1qTagCfgDisable=_WfDot1qTagCfgDisable_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,2),_WfDot1qTagCfgDisable_Type())
wfDot1qTagCfgDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgDisable.setStatus(_A)
_WfDot1qTagCfgVlanName_Type=DisplayString
_WfDot1qTagCfgVlanName_Object=MibTableColumn
wfDot1qTagCfgVlanName=_WfDot1qTagCfgVlanName_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,3),_WfDot1qTagCfgVlanName_Type())
wfDot1qTagCfgVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgVlanName.setStatus(_A)
class _WfDot1qTagCfgLocalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_WfDot1qTagCfgLocalVlanId_Type.__name__=_B
_WfDot1qTagCfgLocalVlanId_Object=MibTableColumn
wfDot1qTagCfgLocalVlanId=_WfDot1qTagCfgLocalVlanId_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,4),_WfDot1qTagCfgLocalVlanId_Type())
wfDot1qTagCfgLocalVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:wfDot1qTagCfgLocalVlanId.setStatus(_A)
class _WfDot1qTagCfgGlobalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WfDot1qTagCfgGlobalVlanId_Type.__name__=_B
_WfDot1qTagCfgGlobalVlanId_Object=MibTableColumn
wfDot1qTagCfgGlobalVlanId=_WfDot1qTagCfgGlobalVlanId_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,5),_WfDot1qTagCfgGlobalVlanId_Type())
wfDot1qTagCfgGlobalVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgGlobalVlanId.setStatus(_A)
class _WfDot1qTagCfgVirtualPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('tagged',1))
_WfDot1qTagCfgVirtualPortType_Type.__name__=_B
_WfDot1qTagCfgVirtualPortType_Object=MibTableColumn
wfDot1qTagCfgVirtualPortType=_WfDot1qTagCfgVirtualPortType_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,6),_WfDot1qTagCfgVirtualPortType_Type())
wfDot1qTagCfgVirtualPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgVirtualPortType.setStatus(_A)
_WfDot1qTagCfgPhysicalPortId_Type=Integer32
_WfDot1qTagCfgPhysicalPortId_Object=MibTableColumn
wfDot1qTagCfgPhysicalPortId=_WfDot1qTagCfgPhysicalPortId_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,7),_WfDot1qTagCfgPhysicalPortId_Type())
wfDot1qTagCfgPhysicalPortId.setMaxAccess(_G)
if mibBuilder.loadTexts:wfDot1qTagCfgPhysicalPortId.setStatus(_A)
class _WfDot1qTagCfgProtocolType_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1514,65535))
_WfDot1qTagCfgProtocolType_Type.__name__=_B
_WfDot1qTagCfgProtocolType_Object=MibTableColumn
wfDot1qTagCfgProtocolType=_WfDot1qTagCfgProtocolType_Object((1,3,6,1,4,1,18,3,5,1,12,6,1,1,1,8),_WfDot1qTagCfgProtocolType_Type())
wfDot1qTagCfgProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:wfDot1qTagCfgProtocolType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wfDot1qTagConfig':wfDot1qTagConfig,'wfDot1qTagConfigTable':wfDot1qTagConfigTable,'wfDot1qTagConfigEntry':wfDot1qTagConfigEntry,'wfDot1qTagCfgDelete':wfDot1qTagCfgDelete,'wfDot1qTagCfgDisable':wfDot1qTagCfgDisable,'wfDot1qTagCfgVlanName':wfDot1qTagCfgVlanName,_F:wfDot1qTagCfgLocalVlanId,'wfDot1qTagCfgGlobalVlanId':wfDot1qTagCfgGlobalVlanId,'wfDot1qTagCfgVirtualPortType':wfDot1qTagCfgVirtualPortType,_E:wfDot1qTagCfgPhysicalPortId,'wfDot1qTagCfgProtocolType':wfDot1qTagCfgProtocolType})