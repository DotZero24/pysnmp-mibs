_L='cpqExExternalStatusIndex'
_K='cpqExOsCommonModuleIndex'
_J='OctetString'
_I='CPQEXTERNAL-MIB'
_H='failed'
_G='degraded'
_F='other'
_E='deprecated'
_D='DisplayString'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_CpqExternalMgmt_ObjectIdentity=ObjectIdentity
cpqExternalMgmt=_CpqExternalMgmt_ObjectIdentity((1,3,6,1,4,1,232,17))
_CpqExMibRev_ObjectIdentity=ObjectIdentity
cpqExMibRev=_CpqExMibRev_ObjectIdentity((1,3,6,1,4,1,232,17,1))
class _CpqExMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqExMibRevMajor_Type.__name__=_C
_CpqExMibRevMajor_Object=MibScalar
cpqExMibRevMajor=_CpqExMibRevMajor_Object((1,3,6,1,4,1,232,17,1,1),_CpqExMibRevMajor_Type())
cpqExMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExMibRevMajor.setStatus(_B)
class _CpqExMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqExMibRevMinor_Type.__name__=_C
_CpqExMibRevMinor_Object=MibScalar
cpqExMibRevMinor=_CpqExMibRevMinor_Object((1,3,6,1,4,1,232,17,1,2),_CpqExMibRevMinor_Type())
cpqExMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExMibRevMinor.setStatus(_B)
class _CpqExMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_G,3),(_H,4)))
_CpqExMibCondition_Type.__name__=_C
_CpqExMibCondition_Object=MibScalar
cpqExMibCondition=_CpqExMibCondition_Object((1,3,6,1,4,1,232,17,1,3),_CpqExMibCondition_Type())
cpqExMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExMibCondition.setStatus(_B)
_CpqExComponent_ObjectIdentity=ObjectIdentity
cpqExComponent=_CpqExComponent_ObjectIdentity((1,3,6,1,4,1,232,17,2))
_CpqExInterface_ObjectIdentity=ObjectIdentity
cpqExInterface=_CpqExInterface_ObjectIdentity((1,3,6,1,4,1,232,17,2,1))
_CpqExOsCommon_ObjectIdentity=ObjectIdentity
cpqExOsCommon=_CpqExOsCommon_ObjectIdentity((1,3,6,1,4,1,232,17,2,1,4))
class _CpqExOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqExOsCommonPollFreq_Type.__name__=_C
_CpqExOsCommonPollFreq_Object=MibScalar
cpqExOsCommonPollFreq=_CpqExOsCommonPollFreq_Object((1,3,6,1,4,1,232,17,2,1,4,1),_CpqExOsCommonPollFreq_Type())
cpqExOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqExOsCommonPollFreq.setStatus(_B)
_CpqExOsCommonModuleTable_Object=MibTable
cpqExOsCommonModuleTable=_CpqExOsCommonModuleTable_Object((1,3,6,1,4,1,232,17,2,1,4,2))
if mibBuilder.loadTexts:cpqExOsCommonModuleTable.setStatus(_E)
_CpqExOsCommonModuleEntry_Object=MibTableRow
cpqExOsCommonModuleEntry=_CpqExOsCommonModuleEntry_Object((1,3,6,1,4,1,232,17,2,1,4,2,1))
cpqExOsCommonModuleEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:cpqExOsCommonModuleEntry.setStatus(_E)
class _CpqExOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqExOsCommonModuleIndex_Type.__name__=_C
_CpqExOsCommonModuleIndex_Object=MibTableColumn
cpqExOsCommonModuleIndex=_CpqExOsCommonModuleIndex_Object((1,3,6,1,4,1,232,17,2,1,4,2,1,1),_CpqExOsCommonModuleIndex_Type())
cpqExOsCommonModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExOsCommonModuleIndex.setStatus(_E)
class _CpqExOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqExOsCommonModuleName_Type.__name__=_D
_CpqExOsCommonModuleName_Object=MibTableColumn
cpqExOsCommonModuleName=_CpqExOsCommonModuleName_Object((1,3,6,1,4,1,232,17,2,1,4,2,1,2),_CpqExOsCommonModuleName_Type())
cpqExOsCommonModuleName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExOsCommonModuleName.setStatus(_E)
class _CpqExOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqExOsCommonModuleVersion_Type.__name__=_D
_CpqExOsCommonModuleVersion_Object=MibTableColumn
cpqExOsCommonModuleVersion=_CpqExOsCommonModuleVersion_Object((1,3,6,1,4,1,232,17,2,1,4,2,1,3),_CpqExOsCommonModuleVersion_Type())
cpqExOsCommonModuleVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExOsCommonModuleVersion.setStatus(_E)
class _CpqExOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqExOsCommonModuleDate_Type.__name__=_J
_CpqExOsCommonModuleDate_Object=MibTableColumn
cpqExOsCommonModuleDate=_CpqExOsCommonModuleDate_Object((1,3,6,1,4,1,232,17,2,1,4,2,1,4),_CpqExOsCommonModuleDate_Type())
cpqExOsCommonModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExOsCommonModuleDate.setStatus(_E)
class _CpqExOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqExOsCommonModulePurpose_Type.__name__=_D
_CpqExOsCommonModulePurpose_Object=MibTableColumn
cpqExOsCommonModulePurpose=_CpqExOsCommonModulePurpose_Object((1,3,6,1,4,1,232,17,2,1,4,2,1,5),_CpqExOsCommonModulePurpose_Type())
cpqExOsCommonModulePurpose.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExOsCommonModulePurpose.setStatus(_E)
_CpqExStatus_ObjectIdentity=ObjectIdentity
cpqExStatus=_CpqExStatus_ObjectIdentity((1,3,6,1,4,1,232,17,2,2))
class _CpqExExternalCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_G,3),(_H,4)))
_CpqExExternalCondition_Type.__name__=_C
_CpqExExternalCondition_Object=MibScalar
cpqExExternalCondition=_CpqExExternalCondition_Object((1,3,6,1,4,1,232,17,2,2,1),_CpqExExternalCondition_Type())
cpqExExternalCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalCondition.setStatus(_B)
_CpqExExternalStatusTable_Object=MibTable
cpqExExternalStatusTable=_CpqExExternalStatusTable_Object((1,3,6,1,4,1,232,17,2,2,2))
if mibBuilder.loadTexts:cpqExExternalStatusTable.setStatus(_B)
_CpqExExternalStatusEntry_Object=MibTableRow
cpqExExternalStatusEntry=_CpqExExternalStatusEntry_Object((1,3,6,1,4,1,232,17,2,2,2,1))
cpqExExternalStatusEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:cpqExExternalStatusEntry.setStatus(_B)
_CpqExExternalStatusIndex_Type=Integer32
_CpqExExternalStatusIndex_Object=MibTableColumn
cpqExExternalStatusIndex=_CpqExExternalStatusIndex_Object((1,3,6,1,4,1,232,17,2,2,2,1,1),_CpqExExternalStatusIndex_Type())
cpqExExternalStatusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusIndex.setStatus(_B)
_CpqExExternalStatusInterval_Type=Integer32
_CpqExExternalStatusInterval_Object=MibTableColumn
cpqExExternalStatusInterval=_CpqExExternalStatusInterval_Object((1,3,6,1,4,1,232,17,2,2,2,1,2),_CpqExExternalStatusInterval_Type())
cpqExExternalStatusInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusInterval.setStatus(_B)
_CpqExExternalStatusVariable_Type=ObjectIdentifier
_CpqExExternalStatusVariable_Object=MibTableColumn
cpqExExternalStatusVariable=_CpqExExternalStatusVariable_Object((1,3,6,1,4,1,232,17,2,2,2,1,3),_CpqExExternalStatusVariable_Type())
cpqExExternalStatusVariable.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusVariable.setStatus(_B)
class _CpqExExternalStatusValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_CpqExExternalStatusValid_Type.__name__=_C
_CpqExExternalStatusValid_Object=MibTableColumn
cpqExExternalStatusValid=_CpqExExternalStatusValid_Object((1,3,6,1,4,1,232,17,2,2,2,1,4),_CpqExExternalStatusValid_Type())
cpqExExternalStatusValid.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusValid.setStatus(_B)
_CpqExExternalStatusValue_Type=Integer32
_CpqExExternalStatusValue_Object=MibTableColumn
cpqExExternalStatusValue=_CpqExExternalStatusValue_Object((1,3,6,1,4,1,232,17,2,2,2,1,5),_CpqExExternalStatusValue_Type())
cpqExExternalStatusValue.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusValue.setStatus(_B)
class _CpqExExternalStatusCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_G,3),(_H,4)))
_CpqExExternalStatusCondition_Type.__name__=_C
_CpqExExternalStatusCondition_Object=MibTableColumn
cpqExExternalStatusCondition=_CpqExExternalStatusCondition_Object((1,3,6,1,4,1,232,17,2,2,2,1,6),_CpqExExternalStatusCondition_Type())
cpqExExternalStatusCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusCondition.setStatus(_B)
class _CpqExExternalStatusOkValues_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqExExternalStatusOkValues_Type.__name__=_D
_CpqExExternalStatusOkValues_Object=MibTableColumn
cpqExExternalStatusOkValues=_CpqExExternalStatusOkValues_Object((1,3,6,1,4,1,232,17,2,2,2,1,7),_CpqExExternalStatusOkValues_Type())
cpqExExternalStatusOkValues.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusOkValues.setStatus(_B)
class _CpqExExternalStatusDegradedValues_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqExExternalStatusDegradedValues_Type.__name__=_D
_CpqExExternalStatusDegradedValues_Object=MibTableColumn
cpqExExternalStatusDegradedValues=_CpqExExternalStatusDegradedValues_Object((1,3,6,1,4,1,232,17,2,2,2,1,8),_CpqExExternalStatusDegradedValues_Type())
cpqExExternalStatusDegradedValues.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusDegradedValues.setStatus(_B)
class _CpqExExternalStatusFailedValues_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqExExternalStatusFailedValues_Type.__name__=_D
_CpqExExternalStatusFailedValues_Object=MibTableColumn
cpqExExternalStatusFailedValues=_CpqExExternalStatusFailedValues_Object((1,3,6,1,4,1,232,17,2,2,2,1,9),_CpqExExternalStatusFailedValues_Type())
cpqExExternalStatusFailedValues.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqExExternalStatusFailedValues.setStatus(_B)
mibBuilder.exportSymbols(_I,**{'cpqExternalMgmt':cpqExternalMgmt,'cpqExMibRev':cpqExMibRev,'cpqExMibRevMajor':cpqExMibRevMajor,'cpqExMibRevMinor':cpqExMibRevMinor,'cpqExMibCondition':cpqExMibCondition,'cpqExComponent':cpqExComponent,'cpqExInterface':cpqExInterface,'cpqExOsCommon':cpqExOsCommon,'cpqExOsCommonPollFreq':cpqExOsCommonPollFreq,'cpqExOsCommonModuleTable':cpqExOsCommonModuleTable,'cpqExOsCommonModuleEntry':cpqExOsCommonModuleEntry,_K:cpqExOsCommonModuleIndex,'cpqExOsCommonModuleName':cpqExOsCommonModuleName,'cpqExOsCommonModuleVersion':cpqExOsCommonModuleVersion,'cpqExOsCommonModuleDate':cpqExOsCommonModuleDate,'cpqExOsCommonModulePurpose':cpqExOsCommonModulePurpose,'cpqExStatus':cpqExStatus,'cpqExExternalCondition':cpqExExternalCondition,'cpqExExternalStatusTable':cpqExExternalStatusTable,'cpqExExternalStatusEntry':cpqExExternalStatusEntry,_L:cpqExExternalStatusIndex,'cpqExExternalStatusInterval':cpqExExternalStatusInterval,'cpqExExternalStatusVariable':cpqExExternalStatusVariable,'cpqExExternalStatusValid':cpqExExternalStatusValid,'cpqExExternalStatusValue':cpqExExternalStatusValue,'cpqExExternalStatusCondition':cpqExExternalStatusCondition,'cpqExExternalStatusOkValues':cpqExExternalStatusOkValues,'cpqExExternalStatusDegradedValues':cpqExExternalStatusDegradedValues,'cpqExExternalStatusFailedValues':cpqExExternalStatusFailedValues})