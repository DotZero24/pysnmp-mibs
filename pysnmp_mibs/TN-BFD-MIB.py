_P='tnBfdAdminTemplateName'
_O='centiseconds'
_N='not-accessible'
_M='tnBfdOperTemplateName'
_L='TimeInterval'
_K='DisplayString'
_J='read-write'
_I='TN-BFD-MIB'
_H='tnSysSwitchId'
_G='TROPIC-SYSTEM-MIB'
_F='Integer32'
_E='read-create'
_D='milliseconds'
_C='read-only'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention',_L)
TNamedItem,=mibBuilder.importSymbols('TN-TC-MIB','TNamedItem')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_G,_H)
tnBfdMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,85))
if mibBuilder.loadTexts:tnBfdMIBModule.setRevisions(('2015-09-30 00:00',))
_TnBfdObjects_ObjectIdentity=ObjectIdentity
tnBfdObjects=_TnBfdObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85))
_TnBfdOperObjects_ObjectIdentity=ObjectIdentity
tnBfdOperObjects=_TnBfdOperObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85,1))
_TnBfdOperValueObjects_ObjectIdentity=ObjectIdentity
tnBfdOperValueObjects=_TnBfdOperValueObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85,1,1))
_TnBfdOperTemplateTable_Object=MibTable
tnBfdOperTemplateTable=_TnBfdOperTemplateTable_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1))
if mibBuilder.loadTexts:tnBfdOperTemplateTable.setStatus(_A)
_TnBfdOperTemplateEntry_Object=MibTableRow
tnBfdOperTemplateEntry=_TnBfdOperTemplateEntry_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1))
tnBfdOperTemplateEntry.setIndexNames((0,_G,_H),(0,_I,_M))
if mibBuilder.loadTexts:tnBfdOperTemplateEntry.setStatus(_A)
_TnBfdOperTemplateName_Type=TNamedItem
_TnBfdOperTemplateName_Object=MibTableColumn
tnBfdOperTemplateName=_TnBfdOperTemplateName_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,1),_TnBfdOperTemplateName_Type())
tnBfdOperTemplateName.setMaxAccess(_N)
if mibBuilder.loadTexts:tnBfdOperTemplateName.setStatus(_A)
_TnBfdOperTemplateRowStatus_Type=RowStatus
_TnBfdOperTemplateRowStatus_Object=MibTableColumn
tnBfdOperTemplateRowStatus=_TnBfdOperTemplateRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,2),_TnBfdOperTemplateRowStatus_Type())
tnBfdOperTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateRowStatus.setStatus(_A)
class _TnBfdOperTemplateTxInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_TnBfdOperTemplateTxInt_Type.__name__=_B
_TnBfdOperTemplateTxInt_Object=MibTableColumn
tnBfdOperTemplateTxInt=_TnBfdOperTemplateTxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,3),_TnBfdOperTemplateTxInt_Type())
tnBfdOperTemplateTxInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateTxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdOperTemplateTxInt.setUnits(_D)
class _TnBfdOperTemplateRxInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_TnBfdOperTemplateRxInt_Type.__name__=_B
_TnBfdOperTemplateRxInt_Object=MibTableColumn
tnBfdOperTemplateRxInt=_TnBfdOperTemplateRxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,4),_TnBfdOperTemplateRxInt_Type())
tnBfdOperTemplateRxInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateRxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdOperTemplateRxInt.setUnits(_D)
class _TnBfdOperTemplateMultiplier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_TnBfdOperTemplateMultiplier_Type.__name__=_B
_TnBfdOperTemplateMultiplier_Object=MibTableColumn
tnBfdOperTemplateMultiplier=_TnBfdOperTemplateMultiplier_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,5),_TnBfdOperTemplateMultiplier_Type())
tnBfdOperTemplateMultiplier.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateMultiplier.setStatus(_A)
class _TnBfdOperTemplateEchoRxInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100000))
_TnBfdOperTemplateEchoRxInt_Type.__name__=_B
_TnBfdOperTemplateEchoRxInt_Object=MibTableColumn
tnBfdOperTemplateEchoRxInt=_TnBfdOperTemplateEchoRxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,6),_TnBfdOperTemplateEchoRxInt_Type())
tnBfdOperTemplateEchoRxInt.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateEchoRxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdOperTemplateEchoRxInt.setUnits(_D)
class _TnBfdOperTemplateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cpmNp',1),('auto',2),('iomHw',3)))
_TnBfdOperTemplateType_Type.__name__=_F
_TnBfdOperTemplateType_Object=MibTableColumn
tnBfdOperTemplateType=_TnBfdOperTemplateType_Object((1,3,6,1,4,1,7483,6,1,2,85,1,1,1,1,7),_TnBfdOperTemplateType_Type())
tnBfdOperTemplateType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdOperTemplateType.setStatus(_A)
_TnBfdAdminObjects_ObjectIdentity=ObjectIdentity
tnBfdAdminObjects=_TnBfdAdminObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85,2))
_TnBfdAdminControlObjects_ObjectIdentity=ObjectIdentity
tnBfdAdminControlObjects=_TnBfdAdminControlObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85,2,1))
class _TnBfdAdminOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TnBfdAdminOwner_Type.__name__=_K
_TnBfdAdminOwner_Object=MibScalar
tnBfdAdminOwner=_TnBfdAdminOwner_Object((1,3,6,1,4,1,7483,6,1,2,85,2,1,1),_TnBfdAdminOwner_Type())
tnBfdAdminOwner.setMaxAccess(_J)
if mibBuilder.loadTexts:tnBfdAdminOwner.setStatus(_A)
class _TnBfdAdminControlApply_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('initialize',2),('commit',3)))
_TnBfdAdminControlApply_Type.__name__=_F
_TnBfdAdminControlApply_Object=MibScalar
tnBfdAdminControlApply=_TnBfdAdminControlApply_Object((1,3,6,1,4,1,7483,6,1,2,85,2,1,2),_TnBfdAdminControlApply_Type())
tnBfdAdminControlApply.setMaxAccess(_J)
if mibBuilder.loadTexts:tnBfdAdminControlApply.setStatus(_A)
_TnBfdAdminLastSetTimer_Type=TimeInterval
_TnBfdAdminLastSetTimer_Object=MibScalar
tnBfdAdminLastSetTimer=_TnBfdAdminLastSetTimer_Object((1,3,6,1,4,1,7483,6,1,2,85,2,1,3),_TnBfdAdminLastSetTimer_Type())
tnBfdAdminLastSetTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdAdminLastSetTimer.setStatus(_A)
if mibBuilder.loadTexts:tnBfdAdminLastSetTimer.setUnits(_O)
class _TnBfdAdminLastSetTimeout_Type(TimeInterval):defaultValue=180000
_TnBfdAdminLastSetTimeout_Type.__name__=_L
_TnBfdAdminLastSetTimeout_Object=MibScalar
tnBfdAdminLastSetTimeout=_TnBfdAdminLastSetTimeout_Object((1,3,6,1,4,1,7483,6,1,2,85,2,1,4),_TnBfdAdminLastSetTimeout_Type())
tnBfdAdminLastSetTimeout.setMaxAccess(_J)
if mibBuilder.loadTexts:tnBfdAdminLastSetTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnBfdAdminLastSetTimeout.setUnits(_O)
_TnBfdAdminValueObjects_ObjectIdentity=ObjectIdentity
tnBfdAdminValueObjects=_TnBfdAdminValueObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,85,2,2))
_TnBfdAdminTemplateTable_Object=MibTable
tnBfdAdminTemplateTable=_TnBfdAdminTemplateTable_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1))
if mibBuilder.loadTexts:tnBfdAdminTemplateTable.setStatus(_A)
_TnBfdAdminTemplateEntry_Object=MibTableRow
tnBfdAdminTemplateEntry=_TnBfdAdminTemplateEntry_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1))
tnBfdAdminTemplateEntry.setIndexNames((0,_G,_H),(0,_I,_P))
if mibBuilder.loadTexts:tnBfdAdminTemplateEntry.setStatus(_A)
_TnBfdAdminTemplateName_Type=TNamedItem
_TnBfdAdminTemplateName_Object=MibTableColumn
tnBfdAdminTemplateName=_TnBfdAdminTemplateName_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,1),_TnBfdAdminTemplateName_Type())
tnBfdAdminTemplateName.setMaxAccess(_N)
if mibBuilder.loadTexts:tnBfdAdminTemplateName.setStatus(_A)
_TnBfdAdminTemplateRowStatus_Type=RowStatus
_TnBfdAdminTemplateRowStatus_Object=MibTableColumn
tnBfdAdminTemplateRowStatus=_TnBfdAdminTemplateRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,2),_TnBfdAdminTemplateRowStatus_Type())
tnBfdAdminTemplateRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateRowStatus.setStatus(_A)
class _TnBfdAdminTemplateTxInt_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,3),ValueRangeConstraint(10,100000))
_TnBfdAdminTemplateTxInt_Type.__name__=_B
_TnBfdAdminTemplateTxInt_Object=MibTableColumn
tnBfdAdminTemplateTxInt=_TnBfdAdminTemplateTxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,3),_TnBfdAdminTemplateTxInt_Type())
tnBfdAdminTemplateTxInt.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateTxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdAdminTemplateTxInt.setUnits(_D)
class _TnBfdAdminTemplateRxInt_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,3),ValueRangeConstraint(10,100000))
_TnBfdAdminTemplateRxInt_Type.__name__=_B
_TnBfdAdminTemplateRxInt_Object=MibTableColumn
tnBfdAdminTemplateRxInt=_TnBfdAdminTemplateRxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,4),_TnBfdAdminTemplateRxInt_Type())
tnBfdAdminTemplateRxInt.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateRxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdAdminTemplateRxInt.setUnits(_D)
class _TnBfdAdminTemplateMultiplier_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_TnBfdAdminTemplateMultiplier_Type.__name__=_B
_TnBfdAdminTemplateMultiplier_Object=MibTableColumn
tnBfdAdminTemplateMultiplier=_TnBfdAdminTemplateMultiplier_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,5),_TnBfdAdminTemplateMultiplier_Type())
tnBfdAdminTemplateMultiplier.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateMultiplier.setStatus(_A)
class _TnBfdAdminTemplateEchoRxInt_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100000))
_TnBfdAdminTemplateEchoRxInt_Type.__name__=_B
_TnBfdAdminTemplateEchoRxInt_Object=MibTableColumn
tnBfdAdminTemplateEchoRxInt=_TnBfdAdminTemplateEchoRxInt_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,6),_TnBfdAdminTemplateEchoRxInt_Type())
tnBfdAdminTemplateEchoRxInt.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateEchoRxInt.setStatus(_A)
if mibBuilder.loadTexts:tnBfdAdminTemplateEchoRxInt.setUnits(_D)
class _TnBfdAdminTemplateType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cpmNp',1),('auto',2),('iomHw',3)))
_TnBfdAdminTemplateType_Type.__name__=_F
_TnBfdAdminTemplateType_Object=MibTableColumn
tnBfdAdminTemplateType=_TnBfdAdminTemplateType_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,1,1,7),_TnBfdAdminTemplateType_Type())
tnBfdAdminTemplateType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnBfdAdminTemplateType.setStatus(_A)
_TnBfdAdminValueScalar1_Type=Unsigned32
_TnBfdAdminValueScalar1_Object=MibScalar
tnBfdAdminValueScalar1=_TnBfdAdminValueScalar1_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,101),_TnBfdAdminValueScalar1_Type())
tnBfdAdminValueScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdAdminValueScalar1.setStatus(_A)
_TnBfdAdminValueScalar2_Type=Unsigned32
_TnBfdAdminValueScalar2_Object=MibScalar
tnBfdAdminValueScalar2=_TnBfdAdminValueScalar2_Object((1,3,6,1,4,1,7483,6,1,2,85,2,2,102),_TnBfdAdminValueScalar2_Type())
tnBfdAdminValueScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnBfdAdminValueScalar2.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'tnBfdMIBModule':tnBfdMIBModule,'tnBfdObjects':tnBfdObjects,'tnBfdOperObjects':tnBfdOperObjects,'tnBfdOperValueObjects':tnBfdOperValueObjects,'tnBfdOperTemplateTable':tnBfdOperTemplateTable,'tnBfdOperTemplateEntry':tnBfdOperTemplateEntry,_M:tnBfdOperTemplateName,'tnBfdOperTemplateRowStatus':tnBfdOperTemplateRowStatus,'tnBfdOperTemplateTxInt':tnBfdOperTemplateTxInt,'tnBfdOperTemplateRxInt':tnBfdOperTemplateRxInt,'tnBfdOperTemplateMultiplier':tnBfdOperTemplateMultiplier,'tnBfdOperTemplateEchoRxInt':tnBfdOperTemplateEchoRxInt,'tnBfdOperTemplateType':tnBfdOperTemplateType,'tnBfdAdminObjects':tnBfdAdminObjects,'tnBfdAdminControlObjects':tnBfdAdminControlObjects,'tnBfdAdminOwner':tnBfdAdminOwner,'tnBfdAdminControlApply':tnBfdAdminControlApply,'tnBfdAdminLastSetTimer':tnBfdAdminLastSetTimer,'tnBfdAdminLastSetTimeout':tnBfdAdminLastSetTimeout,'tnBfdAdminValueObjects':tnBfdAdminValueObjects,'tnBfdAdminTemplateTable':tnBfdAdminTemplateTable,'tnBfdAdminTemplateEntry':tnBfdAdminTemplateEntry,_P:tnBfdAdminTemplateName,'tnBfdAdminTemplateRowStatus':tnBfdAdminTemplateRowStatus,'tnBfdAdminTemplateTxInt':tnBfdAdminTemplateTxInt,'tnBfdAdminTemplateRxInt':tnBfdAdminTemplateRxInt,'tnBfdAdminTemplateMultiplier':tnBfdAdminTemplateMultiplier,'tnBfdAdminTemplateEchoRxInt':tnBfdAdminTemplateEchoRxInt,'tnBfdAdminTemplateType':tnBfdAdminTemplateType,'tnBfdAdminValueScalar1':tnBfdAdminValueScalar1,'tnBfdAdminValueScalar2':tnBfdAdminValueScalar2})