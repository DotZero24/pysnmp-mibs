_H='cpqICAOsCommonModuleIndex'
_G='CPQICA-MIB'
_F='NotificationType'
_E='OctetString'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols('CPQHOST-MIB','compaq','cpqHoTrapFlags')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_CpqICA_ObjectIdentity=ObjectIdentity
cpqICA=_CpqICA_ObjectIdentity((1,3,6,1,4,1,232,140))
_CpqICAMibRev_ObjectIdentity=ObjectIdentity
cpqICAMibRev=_CpqICAMibRev_ObjectIdentity((1,3,6,1,4,1,232,140,1))
class _CpqICAMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqICAMibRevMajor_Type.__name__=_C
_CpqICAMibRevMajor_Object=MibScalar
cpqICAMibRevMajor=_CpqICAMibRevMajor_Object((1,3,6,1,4,1,232,140,1,1),_CpqICAMibRevMajor_Type())
cpqICAMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAMibRevMajor.setStatus(_A)
class _CpqICAMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqICAMibRevMinor_Type.__name__=_C
_CpqICAMibRevMinor_Object=MibScalar
cpqICAMibRevMinor=_CpqICAMibRevMinor_Object((1,3,6,1,4,1,232,140,1,2),_CpqICAMibRevMinor_Type())
cpqICAMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAMibRevMinor.setStatus(_A)
class _CpqICAMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_CpqICAMibCondition_Type.__name__=_C
_CpqICAMibCondition_Object=MibScalar
cpqICAMibCondition=_CpqICAMibCondition_Object((1,3,6,1,4,1,232,140,1,3),_CpqICAMibCondition_Type())
cpqICAMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAMibCondition.setStatus(_A)
_CpqICAComponent_ObjectIdentity=ObjectIdentity
cpqICAComponent=_CpqICAComponent_ObjectIdentity((1,3,6,1,4,1,232,140,2))
_CpqICAInterface_ObjectIdentity=ObjectIdentity
cpqICAInterface=_CpqICAInterface_ObjectIdentity((1,3,6,1,4,1,232,140,2,1))
_CpqICAOsCommon_ObjectIdentity=ObjectIdentity
cpqICAOsCommon=_CpqICAOsCommon_ObjectIdentity((1,3,6,1,4,1,232,140,2,1,4))
class _CpqICAOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqICAOsCommonPollFreq_Type.__name__=_C
_CpqICAOsCommonPollFreq_Object=MibScalar
cpqICAOsCommonPollFreq=_CpqICAOsCommonPollFreq_Object((1,3,6,1,4,1,232,140,2,1,4,1),_CpqICAOsCommonPollFreq_Type())
cpqICAOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqICAOsCommonPollFreq.setStatus(_A)
_CpqICAOsCommonModuleTable_Object=MibTable
cpqICAOsCommonModuleTable=_CpqICAOsCommonModuleTable_Object((1,3,6,1,4,1,232,140,2,1,4,2))
if mibBuilder.loadTexts:cpqICAOsCommonModuleTable.setStatus(_A)
_CpqICAOsCommonModuleEntry_Object=MibTableRow
cpqICAOsCommonModuleEntry=_CpqICAOsCommonModuleEntry_Object((1,3,6,1,4,1,232,140,2,1,4,2,1))
cpqICAOsCommonModuleEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cpqICAOsCommonModuleEntry.setStatus(_A)
class _CpqICAOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqICAOsCommonModuleIndex_Type.__name__=_C
_CpqICAOsCommonModuleIndex_Object=MibTableColumn
cpqICAOsCommonModuleIndex=_CpqICAOsCommonModuleIndex_Object((1,3,6,1,4,1,232,140,2,1,4,2,1,1),_CpqICAOsCommonModuleIndex_Type())
cpqICAOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAOsCommonModuleIndex.setStatus(_A)
class _CpqICAOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqICAOsCommonModuleName_Type.__name__=_D
_CpqICAOsCommonModuleName_Object=MibTableColumn
cpqICAOsCommonModuleName=_CpqICAOsCommonModuleName_Object((1,3,6,1,4,1,232,140,2,1,4,2,1,2),_CpqICAOsCommonModuleName_Type())
cpqICAOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAOsCommonModuleName.setStatus(_A)
class _CpqICAOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqICAOsCommonModuleVersion_Type.__name__=_D
_CpqICAOsCommonModuleVersion_Object=MibTableColumn
cpqICAOsCommonModuleVersion=_CpqICAOsCommonModuleVersion_Object((1,3,6,1,4,1,232,140,2,1,4,2,1,3),_CpqICAOsCommonModuleVersion_Type())
cpqICAOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAOsCommonModuleVersion.setStatus(_A)
class _CpqICAOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqICAOsCommonModuleDate_Type.__name__=_E
_CpqICAOsCommonModuleDate_Object=MibTableColumn
cpqICAOsCommonModuleDate=_CpqICAOsCommonModuleDate_Object((1,3,6,1,4,1,232,140,2,1,4,2,1,4),_CpqICAOsCommonModuleDate_Type())
cpqICAOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAOsCommonModuleDate.setStatus(_A)
class _CpqICAOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqICAOsCommonModulePurpose_Type.__name__=_D
_CpqICAOsCommonModulePurpose_Object=MibTableColumn
cpqICAOsCommonModulePurpose=_CpqICAOsCommonModulePurpose_Object((1,3,6,1,4,1,232,140,2,1,4,2,1,5),_CpqICAOsCommonModulePurpose_Type())
cpqICAOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqICAOsCommonModulePurpose.setStatus(_A)
_CpqICAICA_ObjectIdentity=ObjectIdentity
cpqICAICA=_CpqICAICA_ObjectIdentity((1,3,6,1,4,1,232,140,2,2))
cpqICAAdd=NotificationType((1,3,6,1,4,1,232,0,140001))
if mibBuilder.loadTexts:cpqICAAdd.setStatus('')
cpqICADelete=NotificationType((1,3,6,1,4,1,232,0,140002))
if mibBuilder.loadTexts:cpqICADelete.setStatus('')
cpqICAPropertyChange=NotificationType((1,3,6,1,4,1,232,0,140003))
if mibBuilder.loadTexts:cpqICAPropertyChange.setStatus('')
cpqICAMove=NotificationType((1,3,6,1,4,1,232,0,140004))
if mibBuilder.loadTexts:cpqICAMove.setStatus('')
cpqICAImportRestoreStart=NotificationType((1,3,6,1,4,1,232,0,140005))
if mibBuilder.loadTexts:cpqICAImportRestoreStart.setStatus('')
cpqICAImportRestoreEnd=NotificationType((1,3,6,1,4,1,232,0,140006))
if mibBuilder.loadTexts:cpqICAImportRestoreEnd.setStatus('')
mibBuilder.exportSymbols(_G,**{'cpqICAAdd':cpqICAAdd,'cpqICADelete':cpqICADelete,'cpqICAPropertyChange':cpqICAPropertyChange,'cpqICAMove':cpqICAMove,'cpqICAImportRestoreStart':cpqICAImportRestoreStart,'cpqICAImportRestoreEnd':cpqICAImportRestoreEnd,'cpqICA':cpqICA,'cpqICAMibRev':cpqICAMibRev,'cpqICAMibRevMajor':cpqICAMibRevMajor,'cpqICAMibRevMinor':cpqICAMibRevMinor,'cpqICAMibCondition':cpqICAMibCondition,'cpqICAComponent':cpqICAComponent,'cpqICAInterface':cpqICAInterface,'cpqICAOsCommon':cpqICAOsCommon,'cpqICAOsCommonPollFreq':cpqICAOsCommonPollFreq,'cpqICAOsCommonModuleTable':cpqICAOsCommonModuleTable,'cpqICAOsCommonModuleEntry':cpqICAOsCommonModuleEntry,_H:cpqICAOsCommonModuleIndex,'cpqICAOsCommonModuleName':cpqICAOsCommonModuleName,'cpqICAOsCommonModuleVersion':cpqICAOsCommonModuleVersion,'cpqICAOsCommonModuleDate':cpqICAOsCommonModuleDate,'cpqICAOsCommonModulePurpose':cpqICAOsCommonModulePurpose,'cpqICAICA':cpqICAICA})