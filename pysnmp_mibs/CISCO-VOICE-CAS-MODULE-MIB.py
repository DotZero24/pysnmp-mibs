_T='cvcmCasBitGroup'
_S='cvcmCasBitRowStatus'
_R='cvcmCasDBitAction'
_Q='cvcmCasCBitAction'
_P='cvcmCasBBitAction'
_O='cvcmCasABitAction'
_N='cvcmABCDOutgoingPattern'
_M='cvcmABCDIncomingPattern'
_L='cvcmCasTemplateName'
_K='cvcmModulePhysicalIndex'
_J='read-only'
_I='cvcmABCDPatternIndex'
_H='cvcmCasTemplateIndex'
_G='cvcmModuleIndex'
_F='not-accessible'
_E='Unsigned32'
_D='CvcmCasBitAction'
_C='read-create'
_B='CISCO-VOICE-CAS-MODULE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVoiceCasModuleMIB=ModuleIdentity((1,3,6,1,4,1,9,9,389))
if mibBuilder.loadTexts:ciscoVoiceCasModuleMIB.setRevisions(('2004-03-15 00:00',))
class CvcmCasPatternBitPosition(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('dBit',0),('cBit',1),('bBit',2),('aBit',3)))
class CvcmCasBitAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('casBitNoAction',1),('casBitSetToZero',2),('casBitSetToOne',3),('casBitInvertBit',4),('casBitInvertABit',5),('casBitInvertBBit',6),('casBitInvertCBit',7),('casBitInvertDBit',8),('casBitABit',9),('casBitBBit',10),('casBitCBit',11),('casBitDBit',12)))
_CiscoVoiceCasModuleNotifs_ObjectIdentity=ObjectIdentity
ciscoVoiceCasModuleNotifs=_CiscoVoiceCasModuleNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,389,0))
_CiscoVoiceCasModuleObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceCasModuleObjects=_CiscoVoiceCasModuleObjects_ObjectIdentity((1,3,6,1,4,1,9,9,389,1))
_CvcmCasConfig_ObjectIdentity=ObjectIdentity
cvcmCasConfig=_CvcmCasConfig_ObjectIdentity((1,3,6,1,4,1,9,9,389,1,1))
_CvcmABCDBitTemplateConfigTable_Object=MibTable
cvcmABCDBitTemplateConfigTable=_CvcmABCDBitTemplateConfigTable_Object((1,3,6,1,4,1,9,9,389,1,1,1))
if mibBuilder.loadTexts:cvcmABCDBitTemplateConfigTable.setStatus(_A)
_CvcmABCDBitTemplateConfigEntry_Object=MibTableRow
cvcmABCDBitTemplateConfigEntry=_CvcmABCDBitTemplateConfigEntry_Object((1,3,6,1,4,1,9,9,389,1,1,1,1))
cvcmABCDBitTemplateConfigEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cvcmABCDBitTemplateConfigEntry.setStatus(_A)
class _CvcmModuleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvcmModuleIndex_Type.__name__=_E
_CvcmModuleIndex_Object=MibTableColumn
cvcmModuleIndex=_CvcmModuleIndex_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,1),_CvcmModuleIndex_Type())
cvcmModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvcmModuleIndex.setStatus(_A)
class _CvcmCasTemplateIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvcmCasTemplateIndex_Type.__name__=_E
_CvcmCasTemplateIndex_Object=MibTableColumn
cvcmCasTemplateIndex=_CvcmCasTemplateIndex_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,2),_CvcmCasTemplateIndex_Type())
cvcmCasTemplateIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvcmCasTemplateIndex.setStatus(_A)
class _CvcmABCDPatternIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CvcmABCDPatternIndex_Type.__name__=_E
_CvcmABCDPatternIndex_Object=MibTableColumn
cvcmABCDPatternIndex=_CvcmABCDPatternIndex_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,3),_CvcmABCDPatternIndex_Type())
cvcmABCDPatternIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvcmABCDPatternIndex.setStatus(_A)
_CvcmModulePhysicalIndex_Type=EntPhysicalIndexOrZero
_CvcmModulePhysicalIndex_Object=MibTableColumn
cvcmModulePhysicalIndex=_CvcmModulePhysicalIndex_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,4),_CvcmModulePhysicalIndex_Type())
cvcmModulePhysicalIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cvcmModulePhysicalIndex.setStatus(_A)
_CvcmCasTemplateName_Type=SnmpAdminString
_CvcmCasTemplateName_Object=MibTableColumn
cvcmCasTemplateName=_CvcmCasTemplateName_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,5),_CvcmCasTemplateName_Type())
cvcmCasTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasTemplateName.setStatus(_A)
_CvcmABCDIncomingPattern_Type=CvcmCasPatternBitPosition
_CvcmABCDIncomingPattern_Object=MibTableColumn
cvcmABCDIncomingPattern=_CvcmABCDIncomingPattern_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,6),_CvcmABCDIncomingPattern_Type())
cvcmABCDIncomingPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmABCDIncomingPattern.setStatus(_A)
_CvcmABCDOutgoingPattern_Type=CvcmCasPatternBitPosition
_CvcmABCDOutgoingPattern_Object=MibTableColumn
cvcmABCDOutgoingPattern=_CvcmABCDOutgoingPattern_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,7),_CvcmABCDOutgoingPattern_Type())
cvcmABCDOutgoingPattern.setMaxAccess(_J)
if mibBuilder.loadTexts:cvcmABCDOutgoingPattern.setStatus(_A)
class _CvcmCasABitAction_Type(CvcmCasBitAction):defaultValue=9
_CvcmCasABitAction_Type.__name__=_D
_CvcmCasABitAction_Object=MibTableColumn
cvcmCasABitAction=_CvcmCasABitAction_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,8),_CvcmCasABitAction_Type())
cvcmCasABitAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasABitAction.setStatus(_A)
class _CvcmCasBBitAction_Type(CvcmCasBitAction):defaultValue=10
_CvcmCasBBitAction_Type.__name__=_D
_CvcmCasBBitAction_Object=MibTableColumn
cvcmCasBBitAction=_CvcmCasBBitAction_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,9),_CvcmCasBBitAction_Type())
cvcmCasBBitAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasBBitAction.setStatus(_A)
class _CvcmCasCBitAction_Type(CvcmCasBitAction):defaultValue=11
_CvcmCasCBitAction_Type.__name__=_D
_CvcmCasCBitAction_Object=MibTableColumn
cvcmCasCBitAction=_CvcmCasCBitAction_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,10),_CvcmCasCBitAction_Type())
cvcmCasCBitAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasCBitAction.setStatus(_A)
class _CvcmCasDBitAction_Type(CvcmCasBitAction):defaultValue=12
_CvcmCasDBitAction_Type.__name__=_D
_CvcmCasDBitAction_Object=MibTableColumn
cvcmCasDBitAction=_CvcmCasDBitAction_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,11),_CvcmCasDBitAction_Type())
cvcmCasDBitAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasDBitAction.setStatus(_A)
_CvcmCasBitRowStatus_Type=RowStatus
_CvcmCasBitRowStatus_Object=MibTableColumn
cvcmCasBitRowStatus=_CvcmCasBitRowStatus_Object((1,3,6,1,4,1,9,9,389,1,1,1,1,12),_CvcmCasBitRowStatus_Type())
cvcmCasBitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcmCasBitRowStatus.setStatus(_A)
_CvcmMIBConformance_ObjectIdentity=ObjectIdentity
cvcmMIBConformance=_CvcmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,389,2))
_CvcmMIBGroups_ObjectIdentity=ObjectIdentity
cvcmMIBGroups=_CvcmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,389,2,1))
_CvcmMIBCompliances_ObjectIdentity=ObjectIdentity
cvcmMIBCompliances=_CvcmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,389,2,2))
cvcmCasBitGroup=ObjectGroup((1,3,6,1,4,1,9,9,389,2,1,1))
cvcmCasBitGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cvcmCasBitGroup.setStatus(_A)
ciscoVoiceCasModuleMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,389,2,2,1))
ciscoVoiceCasModuleMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:ciscoVoiceCasModuleMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvcmCasPatternBitPosition':CvcmCasPatternBitPosition,_D:CvcmCasBitAction,'ciscoVoiceCasModuleMIB':ciscoVoiceCasModuleMIB,'ciscoVoiceCasModuleNotifs':ciscoVoiceCasModuleNotifs,'ciscoVoiceCasModuleObjects':ciscoVoiceCasModuleObjects,'cvcmCasConfig':cvcmCasConfig,'cvcmABCDBitTemplateConfigTable':cvcmABCDBitTemplateConfigTable,'cvcmABCDBitTemplateConfigEntry':cvcmABCDBitTemplateConfigEntry,_G:cvcmModuleIndex,_H:cvcmCasTemplateIndex,_I:cvcmABCDPatternIndex,_K:cvcmModulePhysicalIndex,_L:cvcmCasTemplateName,_M:cvcmABCDIncomingPattern,_N:cvcmABCDOutgoingPattern,_O:cvcmCasABitAction,_P:cvcmCasBBitAction,_Q:cvcmCasCBitAction,_R:cvcmCasDBitAction,_S:cvcmCasBitRowStatus,'cvcmMIBConformance':cvcmMIBConformance,'cvcmMIBGroups':cvcmMIBGroups,_T:cvcmCasBitGroup,'cvcmMIBCompliances':cvcmMIBCompliances,'ciscoVoiceCasModuleMIBCompliance':ciscoVoiceCasModuleMIBCompliance})