_K='rlSmartPortsMacroDescriptionIndex'
_J='rlSmartPortsMacroOctetIndex'
_I='rlSmartPortsMacroIndex'
_H='rlSmartPortsMacroName'
_G='not-accessible'
_F='Integer32'
_E='RADLAN-SMARTPORTS-MIB'
_D='DisplayString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
rlSmartPorts=ModuleIdentity((1,3,6,1,4,1,89,140))
if mibBuilder.loadTexts:rlSmartPorts.setRevisions(('2008-07-30 00:00',))
class MacroType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rlSmartPortsMacroInterfaceVendorProvided',1),('rlSmartPortsMacroGloablVendorProvided',2),('rlSmartPortsMacroUserCreated',3)))
class RlSmartPortsMacroName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class RlSmartPortsMacroNameOrZero(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlSmartPortsMacroManageTable_Object=MibTable
rlSmartPortsMacroManageTable=_RlSmartPortsMacroManageTable_Object((1,3,6,1,4,1,89,140,1))
if mibBuilder.loadTexts:rlSmartPortsMacroManageTable.setStatus(_A)
_RlSmartPortsMacroManageEntry_Object=MibTableRow
rlSmartPortsMacroManageEntry=_RlSmartPortsMacroManageEntry_Object((1,3,6,1,4,1,89,140,1,1))
rlSmartPortsMacroManageEntry.setIndexNames((1,_E,_H))
if mibBuilder.loadTexts:rlSmartPortsMacroManageEntry.setStatus(_A)
_RlSmartPortsMacroName_Type=RlSmartPortsMacroName
_RlSmartPortsMacroName_Object=MibTableColumn
rlSmartPortsMacroName=_RlSmartPortsMacroName_Object((1,3,6,1,4,1,89,140,1,1,1),_RlSmartPortsMacroName_Type())
rlSmartPortsMacroName.setMaxAccess(_G)
if mibBuilder.loadTexts:rlSmartPortsMacroName.setStatus(_A)
_RlSmartPortsMacroIndex_Type=Integer32
_RlSmartPortsMacroIndex_Object=MibTableColumn
rlSmartPortsMacroIndex=_RlSmartPortsMacroIndex_Object((1,3,6,1,4,1,89,140,1,1,2),_RlSmartPortsMacroIndex_Type())
rlSmartPortsMacroIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsMacroIndex.setStatus(_A)
_RlSmartPortsMacroType_Type=MacroType
_RlSmartPortsMacroType_Object=MibTableColumn
rlSmartPortsMacroType=_RlSmartPortsMacroType_Object((1,3,6,1,4,1,89,140,1,1,3),_RlSmartPortsMacroType_Type())
rlSmartPortsMacroType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsMacroType.setStatus(_A)
_RlSmartPortsMacroStatus_Type=RowStatus
_RlSmartPortsMacroStatus_Object=MibTableColumn
rlSmartPortsMacroStatus=_RlSmartPortsMacroStatus_Object((1,3,6,1,4,1,89,140,1,1,4),_RlSmartPortsMacroStatus_Type())
rlSmartPortsMacroStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsMacroStatus.setStatus(_A)
class _RlSmartPortsMacroKeywords_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSmartPortsMacroKeywords_Type.__name__=_D
_RlSmartPortsMacroKeywords_Object=MibTableColumn
rlSmartPortsMacroKeywords=_RlSmartPortsMacroKeywords_Object((1,3,6,1,4,1,89,140,1,1,5),_RlSmartPortsMacroKeywords_Type())
rlSmartPortsMacroKeywords.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsMacroKeywords.setStatus(_A)
class _RlSmartPortsMacroDesc1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSmartPortsMacroDesc1_Type.__name__=_D
_RlSmartPortsMacroDesc1_Object=MibTableColumn
rlSmartPortsMacroDesc1=_RlSmartPortsMacroDesc1_Object((1,3,6,1,4,1,89,140,1,1,6),_RlSmartPortsMacroDesc1_Type())
rlSmartPortsMacroDesc1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsMacroDesc1.setStatus(_A)
class _RlSmartPortsMacroDesc2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlSmartPortsMacroDesc2_Type.__name__=_D
_RlSmartPortsMacroDesc2_Object=MibTableColumn
rlSmartPortsMacroDesc2=_RlSmartPortsMacroDesc2_Object((1,3,6,1,4,1,89,140,1,1,7),_RlSmartPortsMacroDesc2_Type())
rlSmartPortsMacroDesc2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsMacroDesc2.setStatus(_A)
_RlSmartPortsMacroContentTable_Object=MibTable
rlSmartPortsMacroContentTable=_RlSmartPortsMacroContentTable_Object((1,3,6,1,4,1,89,140,2))
if mibBuilder.loadTexts:rlSmartPortsMacroContentTable.setStatus(_A)
_RlSmartPortsMacroContentEntry_Object=MibTableRow
rlSmartPortsMacroContentEntry=_RlSmartPortsMacroContentEntry_Object((1,3,6,1,4,1,89,140,2,1))
rlSmartPortsMacroContentEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:rlSmartPortsMacroContentEntry.setStatus(_A)
class _RlSmartPortsMacroOctetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,19))
_RlSmartPortsMacroOctetIndex_Type.__name__=_F
_RlSmartPortsMacroOctetIndex_Object=MibTableColumn
rlSmartPortsMacroOctetIndex=_RlSmartPortsMacroOctetIndex_Object((1,3,6,1,4,1,89,140,2,1,1),_RlSmartPortsMacroOctetIndex_Type())
rlSmartPortsMacroOctetIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlSmartPortsMacroOctetIndex.setStatus(_A)
_RlSmartPortsMacroText_Type=SnmpAdminString
_RlSmartPortsMacroText_Object=MibTableColumn
rlSmartPortsMacroText=_RlSmartPortsMacroText_Object((1,3,6,1,4,1,89,140,2,1,2),_RlSmartPortsMacroText_Type())
rlSmartPortsMacroText.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsMacroText.setStatus(_A)
_RlSmartPortsMacroDescriptionTable_Object=MibTable
rlSmartPortsMacroDescriptionTable=_RlSmartPortsMacroDescriptionTable_Object((1,3,6,1,4,1,89,140,3))
if mibBuilder.loadTexts:rlSmartPortsMacroDescriptionTable.setStatus(_A)
_RlSmartPortsMacroDescriptionEntry_Object=MibTableRow
rlSmartPortsMacroDescriptionEntry=_RlSmartPortsMacroDescriptionEntry_Object((1,3,6,1,4,1,89,140,3,1))
rlSmartPortsMacroDescriptionEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:rlSmartPortsMacroDescriptionEntry.setStatus(_A)
_RlSmartPortsMacroDescriptionIndex_Type=InterfaceIndexOrZero
_RlSmartPortsMacroDescriptionIndex_Object=MibTableColumn
rlSmartPortsMacroDescriptionIndex=_RlSmartPortsMacroDescriptionIndex_Object((1,3,6,1,4,1,89,140,3,1,1),_RlSmartPortsMacroDescriptionIndex_Type())
rlSmartPortsMacroDescriptionIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlSmartPortsMacroDescriptionIndex.setStatus(_A)
_RlSmartPortsMacroDescriptionText_Type=SnmpAdminString
_RlSmartPortsMacroDescriptionText_Object=MibTableColumn
rlSmartPortsMacroDescriptionText=_RlSmartPortsMacroDescriptionText_Object((1,3,6,1,4,1,89,140,3,1,2),_RlSmartPortsMacroDescriptionText_Type())
rlSmartPortsMacroDescriptionText.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsMacroDescriptionText.setStatus(_A)
_RlSmartPortsMacroDescriptionStatus_Type=RowStatus
_RlSmartPortsMacroDescriptionStatus_Object=MibTableColumn
rlSmartPortsMacroDescriptionStatus=_RlSmartPortsMacroDescriptionStatus_Object((1,3,6,1,4,1,89,140,3,1,3),_RlSmartPortsMacroDescriptionStatus_Type())
rlSmartPortsMacroDescriptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsMacroDescriptionStatus.setStatus(_A)
_RlSmartPortsFreeIndexes_Type=Integer32
_RlSmartPortsFreeIndexes_Object=MibScalar
rlSmartPortsFreeIndexes=_RlSmartPortsFreeIndexes_Object((1,3,6,1,4,1,89,140,4),_RlSmartPortsFreeIndexes_Type())
rlSmartPortsFreeIndexes.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsFreeIndexes.setStatus(_A)
class _RlSmartPortsDiagMacroName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlSmartPortsDiagMacroName_Type.__name__=_D
_RlSmartPortsDiagMacroName_Object=MibScalar
rlSmartPortsDiagMacroName=_RlSmartPortsDiagMacroName_Object((1,3,6,1,4,1,89,140,5),_RlSmartPortsDiagMacroName_Type())
rlSmartPortsDiagMacroName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsDiagMacroName.setStatus(_A)
_RlSmartPortsDiagLineNumber_Type=Integer32
_RlSmartPortsDiagLineNumber_Object=MibScalar
rlSmartPortsDiagLineNumber=_RlSmartPortsDiagLineNumber_Object((1,3,6,1,4,1,89,140,6),_RlSmartPortsDiagLineNumber_Type())
rlSmartPortsDiagLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsDiagLineNumber.setStatus(_A)
_RlSmartPortsDiagCommandLine_Type=SnmpAdminString
_RlSmartPortsDiagCommandLine_Object=MibScalar
rlSmartPortsDiagCommandLine=_RlSmartPortsDiagCommandLine_Object((1,3,6,1,4,1,89,140,7),_RlSmartPortsDiagCommandLine_Type())
rlSmartPortsDiagCommandLine.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSmartPortsDiagCommandLine.setStatus(_A)
class _RlSmartPortsCondenseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlSmartPortsCondenseMode_Type.__name__=_F
_RlSmartPortsCondenseMode_Object=MibScalar
rlSmartPortsCondenseMode=_RlSmartPortsCondenseMode_Object((1,3,6,1,4,1,89,140,8),_RlSmartPortsCondenseMode_Type())
rlSmartPortsCondenseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSmartPortsCondenseMode.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacroType':MacroType,'RlSmartPortsMacroName':RlSmartPortsMacroName,'RlSmartPortsMacroNameOrZero':RlSmartPortsMacroNameOrZero,'rlSmartPorts':rlSmartPorts,'rlSmartPortsMacroManageTable':rlSmartPortsMacroManageTable,'rlSmartPortsMacroManageEntry':rlSmartPortsMacroManageEntry,_H:rlSmartPortsMacroName,_I:rlSmartPortsMacroIndex,'rlSmartPortsMacroType':rlSmartPortsMacroType,'rlSmartPortsMacroStatus':rlSmartPortsMacroStatus,'rlSmartPortsMacroKeywords':rlSmartPortsMacroKeywords,'rlSmartPortsMacroDesc1':rlSmartPortsMacroDesc1,'rlSmartPortsMacroDesc2':rlSmartPortsMacroDesc2,'rlSmartPortsMacroContentTable':rlSmartPortsMacroContentTable,'rlSmartPortsMacroContentEntry':rlSmartPortsMacroContentEntry,_J:rlSmartPortsMacroOctetIndex,'rlSmartPortsMacroText':rlSmartPortsMacroText,'rlSmartPortsMacroDescriptionTable':rlSmartPortsMacroDescriptionTable,'rlSmartPortsMacroDescriptionEntry':rlSmartPortsMacroDescriptionEntry,_K:rlSmartPortsMacroDescriptionIndex,'rlSmartPortsMacroDescriptionText':rlSmartPortsMacroDescriptionText,'rlSmartPortsMacroDescriptionStatus':rlSmartPortsMacroDescriptionStatus,'rlSmartPortsFreeIndexes':rlSmartPortsFreeIndexes,'rlSmartPortsDiagMacroName':rlSmartPortsDiagMacroName,'rlSmartPortsDiagLineNumber':rlSmartPortsDiagLineNumber,'rlSmartPortsDiagCommandLine':rlSmartPortsDiagCommandLine,'rlSmartPortsCondenseMode':rlSmartPortsCondenseMode})