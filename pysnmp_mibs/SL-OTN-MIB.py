_F='slOTNCurrentPmIndex'
_E='slOTNConfigLineIndex'
_D='SL-OTN-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slOTN=ModuleIdentity((1,3,6,1,4,1,4515,1,1,15))
class OTNTraceMessage(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class OTNTrafficRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('sonetSdh10G',1),('gbe10GLan',2),('fc10G',3),('otu2',4),('otu2eLan',5),('otu2eLanStuff',6),('otu2eFc',7),('otu2FcStuff',8)))
class OTNOperationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('async',1),('sync',2),('bypass',3)))
_SlOTNConfig_ObjectIdentity=ObjectIdentity
slOTNConfig=_SlOTNConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,15,1))
_SlOTNConfigTable_Object=MibTable
slOTNConfigTable=_SlOTNConfigTable_Object((1,3,6,1,4,1,4515,1,1,15,1,1))
if mibBuilder.loadTexts:slOTNConfigTable.setStatus(_A)
_SlOTNConfigEntry_Object=MibTableRow
slOTNConfigEntry=_SlOTNConfigEntry_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1))
slOTNConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slOTNConfigEntry.setStatus(_A)
_SlOTNConfigLineIndex_Type=InterfaceIndex
_SlOTNConfigLineIndex_Object=MibTableColumn
slOTNConfigLineIndex=_SlOTNConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,1),_SlOTNConfigLineIndex_Type())
slOTNConfigLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNConfigLineIndex.setStatus(_A)
_SlOTNConfigOperationMode_Type=OTNOperationMode
_SlOTNConfigOperationMode_Object=MibTableColumn
slOTNConfigOperationMode=_SlOTNConfigOperationMode_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,2),_SlOTNConfigOperationMode_Type())
slOTNConfigOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOperationMode.setStatus(_A)
_SlOTNConfigFECEnabled_Type=Integer32
_SlOTNConfigFECEnabled_Object=MibTableColumn
slOTNConfigFECEnabled=_SlOTNConfigFECEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,3),_SlOTNConfigFECEnabled_Type())
slOTNConfigFECEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigFECEnabled.setStatus(_A)
_SlOTNConfigStuffingEnabled_Type=TruthValue
_SlOTNConfigStuffingEnabled_Object=MibTableColumn
slOTNConfigStuffingEnabled=_SlOTNConfigStuffingEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,4),_SlOTNConfigStuffingEnabled_Type())
slOTNConfigStuffingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigStuffingEnabled.setStatus(_A)
_SlOTNConfigOTUkTIMDetEnabled_Type=TruthValue
_SlOTNConfigOTUkTIMDetEnabled_Object=MibTableColumn
slOTNConfigOTUkTIMDetEnabled=_SlOTNConfigOTUkTIMDetEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,5),_SlOTNConfigOTUkTIMDetEnabled_Type())
slOTNConfigOTUkTIMDetEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkTIMDetEnabled.setStatus(_A)
_SlOTNConfigOTUkDAPIToTransmit_Type=OTNTraceMessage
_SlOTNConfigOTUkDAPIToTransmit_Object=MibTableColumn
slOTNConfigOTUkDAPIToTransmit=_SlOTNConfigOTUkDAPIToTransmit_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,6),_SlOTNConfigOTUkDAPIToTransmit_Type())
slOTNConfigOTUkDAPIToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkDAPIToTransmit.setStatus(_A)
_SlOTNConfigOTUkSAPIToTransmit_Type=OTNTraceMessage
_SlOTNConfigOTUkSAPIToTransmit_Object=MibTableColumn
slOTNConfigOTUkSAPIToTransmit=_SlOTNConfigOTUkSAPIToTransmit_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,7),_SlOTNConfigOTUkSAPIToTransmit_Type())
slOTNConfigOTUkSAPIToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkSAPIToTransmit.setStatus(_A)
_SlOTNConfigOTUkDAPIToExpect_Type=OTNTraceMessage
_SlOTNConfigOTUkDAPIToExpect_Object=MibTableColumn
slOTNConfigOTUkDAPIToExpect=_SlOTNConfigOTUkDAPIToExpect_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,8),_SlOTNConfigOTUkDAPIToExpect_Type())
slOTNConfigOTUkDAPIToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkDAPIToExpect.setStatus(_A)
_SlOTNConfigOTUkSAPIToExpect_Type=OTNTraceMessage
_SlOTNConfigOTUkSAPIToExpect_Object=MibTableColumn
slOTNConfigOTUkSAPIToExpect=_SlOTNConfigOTUkSAPIToExpect_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,9),_SlOTNConfigOTUkSAPIToExpect_Type())
slOTNConfigOTUkSAPIToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkSAPIToExpect.setStatus(_A)
_SlOTNConfigOTUkDAPIReceived_Type=OTNTraceMessage
_SlOTNConfigOTUkDAPIReceived_Object=MibTableColumn
slOTNConfigOTUkDAPIReceived=_SlOTNConfigOTUkDAPIReceived_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,10),_SlOTNConfigOTUkDAPIReceived_Type())
slOTNConfigOTUkDAPIReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNConfigOTUkDAPIReceived.setStatus(_A)
_SlOTNConfigOTUkSAPIReceived_Type=OTNTraceMessage
_SlOTNConfigOTUkSAPIReceived_Object=MibTableColumn
slOTNConfigOTUkSAPIReceived=_SlOTNConfigOTUkSAPIReceived_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,11),_SlOTNConfigOTUkSAPIReceived_Type())
slOTNConfigOTUkSAPIReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNConfigOTUkSAPIReceived.setStatus(_A)
_SlOTNConfigODUkTIMDetEnabled_Type=TruthValue
_SlOTNConfigODUkTIMDetEnabled_Object=MibTableColumn
slOTNConfigODUkTIMDetEnabled=_SlOTNConfigODUkTIMDetEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,12),_SlOTNConfigODUkTIMDetEnabled_Type())
slOTNConfigODUkTIMDetEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkTIMDetEnabled.setStatus(_A)
_SlOTNConfigODUkDAPIToTransmit_Type=OTNTraceMessage
_SlOTNConfigODUkDAPIToTransmit_Object=MibTableColumn
slOTNConfigODUkDAPIToTransmit=_SlOTNConfigODUkDAPIToTransmit_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,13),_SlOTNConfigODUkDAPIToTransmit_Type())
slOTNConfigODUkDAPIToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkDAPIToTransmit.setStatus(_A)
_SlOTNConfigODUkSAPIToTransmit_Type=OTNTraceMessage
_SlOTNConfigODUkSAPIToTransmit_Object=MibTableColumn
slOTNConfigODUkSAPIToTransmit=_SlOTNConfigODUkSAPIToTransmit_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,14),_SlOTNConfigODUkSAPIToTransmit_Type())
slOTNConfigODUkSAPIToTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkSAPIToTransmit.setStatus(_A)
_SlOTNConfigODUkDAPIToExpect_Type=OTNTraceMessage
_SlOTNConfigODUkDAPIToExpect_Object=MibTableColumn
slOTNConfigODUkDAPIToExpect=_SlOTNConfigODUkDAPIToExpect_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,15),_SlOTNConfigODUkDAPIToExpect_Type())
slOTNConfigODUkDAPIToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkDAPIToExpect.setStatus(_A)
_SlOTNConfigODUkSAPIToExpect_Type=OTNTraceMessage
_SlOTNConfigODUkSAPIToExpect_Object=MibTableColumn
slOTNConfigODUkSAPIToExpect=_SlOTNConfigODUkSAPIToExpect_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,16),_SlOTNConfigODUkSAPIToExpect_Type())
slOTNConfigODUkSAPIToExpect.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkSAPIToExpect.setStatus(_A)
_SlOTNConfigODUkDAPIReceived_Type=OTNTraceMessage
_SlOTNConfigODUkDAPIReceived_Object=MibTableColumn
slOTNConfigODUkDAPIReceived=_SlOTNConfigODUkDAPIReceived_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,17),_SlOTNConfigODUkDAPIReceived_Type())
slOTNConfigODUkDAPIReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNConfigODUkDAPIReceived.setStatus(_A)
_SlOTNConfigODUkSAPIReceived_Type=OTNTraceMessage
_SlOTNConfigODUkSAPIReceived_Object=MibTableColumn
slOTNConfigODUkSAPIReceived=_SlOTNConfigODUkSAPIReceived_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,18),_SlOTNConfigODUkSAPIReceived_Type())
slOTNConfigODUkSAPIReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNConfigODUkSAPIReceived.setStatus(_A)
_SlOTNConfigOTUkTIMKillEnabled_Type=TruthValue
_SlOTNConfigOTUkTIMKillEnabled_Object=MibTableColumn
slOTNConfigOTUkTIMKillEnabled=_SlOTNConfigOTUkTIMKillEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,19),_SlOTNConfigOTUkTIMKillEnabled_Type())
slOTNConfigOTUkTIMKillEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigOTUkTIMKillEnabled.setStatus(_A)
_SlOTNConfigODUkTIMKillEnabled_Type=TruthValue
_SlOTNConfigODUkTIMKillEnabled_Object=MibTableColumn
slOTNConfigODUkTIMKillEnabled=_SlOTNConfigODUkTIMKillEnabled_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,20),_SlOTNConfigODUkTIMKillEnabled_Type())
slOTNConfigODUkTIMKillEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigODUkTIMKillEnabled.setStatus(_A)
_SlOTNConfigInbandGCC_Type=Integer32
_SlOTNConfigInbandGCC_Object=MibTableColumn
slOTNConfigInbandGCC=_SlOTNConfigInbandGCC_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,21),_SlOTNConfigInbandGCC_Type())
slOTNConfigInbandGCC.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNConfigInbandGCC.setStatus(_A)
_SlOTNMsiDisable_Type=TruthValue
_SlOTNMsiDisable_Object=MibTableColumn
slOTNMsiDisable=_SlOTNMsiDisable_Object((1,3,6,1,4,1,4515,1,1,15,1,1,1,22),_SlOTNMsiDisable_Type())
slOTNMsiDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNMsiDisable.setStatus(_A)
_SlOTNPm_ObjectIdentity=ObjectIdentity
slOTNPm=_SlOTNPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,15,2))
_SlOTNCurrentPmTable_Object=MibTable
slOTNCurrentPmTable=_SlOTNCurrentPmTable_Object((1,3,6,1,4,1,4515,1,1,15,2,1))
if mibBuilder.loadTexts:slOTNCurrentPmTable.setStatus(_A)
_SlOTNCurrentPmEntry_Object=MibTableRow
slOTNCurrentPmEntry=_SlOTNCurrentPmEntry_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1))
slOTNCurrentPmEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:slOTNCurrentPmEntry.setStatus(_A)
_SlOTNCurrentPmIndex_Type=InterfaceIndex
_SlOTNCurrentPmIndex_Object=MibTableColumn
slOTNCurrentPmIndex=_SlOTNCurrentPmIndex_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,1),_SlOTNCurrentPmIndex_Type())
slOTNCurrentPmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmIndex.setStatus(_A)
_SlOTNCurrentPmFecCe_Type=Integer32
_SlOTNCurrentPmFecCe_Object=MibTableColumn
slOTNCurrentPmFecCe=_SlOTNCurrentPmFecCe_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,2),_SlOTNCurrentPmFecCe_Type())
slOTNCurrentPmFecCe.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCe.setStatus(_A)
_SlOTNCurrentPmFecCerMant_Type=Integer32
_SlOTNCurrentPmFecCerMant_Object=MibTableColumn
slOTNCurrentPmFecCerMant=_SlOTNCurrentPmFecCerMant_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,3),_SlOTNCurrentPmFecCerMant_Type())
slOTNCurrentPmFecCerMant.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerMant.setStatus(_A)
_SlOTNCurrentPmFecCerExp_Type=Integer32
_SlOTNCurrentPmFecCerExp_Object=MibTableColumn
slOTNCurrentPmFecCerExp=_SlOTNCurrentPmFecCerExp_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,4),_SlOTNCurrentPmFecCerExp_Type())
slOTNCurrentPmFecCerExp.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerExp.setStatus(_A)
_SlOTNCurrentPmFecCerValid_Type=TruthValue
_SlOTNCurrentPmFecCerValid_Object=MibTableColumn
slOTNCurrentPmFecCerValid=_SlOTNCurrentPmFecCerValid_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,5),_SlOTNCurrentPmFecCerValid_Type())
slOTNCurrentPmFecCerValid.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerValid.setStatus(_A)
_SlOTNCurrentPmFecCerMantFE_Type=Integer32
_SlOTNCurrentPmFecCerMantFE_Object=MibTableColumn
slOTNCurrentPmFecCerMantFE=_SlOTNCurrentPmFecCerMantFE_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,6),_SlOTNCurrentPmFecCerMantFE_Type())
slOTNCurrentPmFecCerMantFE.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerMantFE.setStatus(_A)
_SlOTNCurrentPmFecCerExpFE_Type=Integer32
_SlOTNCurrentPmFecCerExpFE_Object=MibTableColumn
slOTNCurrentPmFecCerExpFE=_SlOTNCurrentPmFecCerExpFE_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,7),_SlOTNCurrentPmFecCerExpFE_Type())
slOTNCurrentPmFecCerExpFE.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerExpFE.setStatus(_A)
_SlOTNCurrentPmFecCerValidFE_Type=TruthValue
_SlOTNCurrentPmFecCerValidFE_Object=MibTableColumn
slOTNCurrentPmFecCerValidFE=_SlOTNCurrentPmFecCerValidFE_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,8),_SlOTNCurrentPmFecCerValidFE_Type())
slOTNCurrentPmFecCerValidFE.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTNCurrentPmFecCerValidFE.setStatus(_A)
_SlOTNCurrentPmReset_Type=Integer32
_SlOTNCurrentPmReset_Object=MibTableColumn
slOTNCurrentPmReset=_SlOTNCurrentPmReset_Object((1,3,6,1,4,1,4515,1,1,15,2,1,1,9),_SlOTNCurrentPmReset_Type())
slOTNCurrentPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTNCurrentPmReset.setStatus(_A)
_SlOTNTraps_ObjectIdentity=ObjectIdentity
slOTNTraps=_SlOTNTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,15,3))
mibBuilder.exportSymbols(_D,**{'OTNTraceMessage':OTNTraceMessage,'OTNTrafficRate':OTNTrafficRate,'OTNOperationMode':OTNOperationMode,'slOTN':slOTN,'slOTNConfig':slOTNConfig,'slOTNConfigTable':slOTNConfigTable,'slOTNConfigEntry':slOTNConfigEntry,_E:slOTNConfigLineIndex,'slOTNConfigOperationMode':slOTNConfigOperationMode,'slOTNConfigFECEnabled':slOTNConfigFECEnabled,'slOTNConfigStuffingEnabled':slOTNConfigStuffingEnabled,'slOTNConfigOTUkTIMDetEnabled':slOTNConfigOTUkTIMDetEnabled,'slOTNConfigOTUkDAPIToTransmit':slOTNConfigOTUkDAPIToTransmit,'slOTNConfigOTUkSAPIToTransmit':slOTNConfigOTUkSAPIToTransmit,'slOTNConfigOTUkDAPIToExpect':slOTNConfigOTUkDAPIToExpect,'slOTNConfigOTUkSAPIToExpect':slOTNConfigOTUkSAPIToExpect,'slOTNConfigOTUkDAPIReceived':slOTNConfigOTUkDAPIReceived,'slOTNConfigOTUkSAPIReceived':slOTNConfigOTUkSAPIReceived,'slOTNConfigODUkTIMDetEnabled':slOTNConfigODUkTIMDetEnabled,'slOTNConfigODUkDAPIToTransmit':slOTNConfigODUkDAPIToTransmit,'slOTNConfigODUkSAPIToTransmit':slOTNConfigODUkSAPIToTransmit,'slOTNConfigODUkDAPIToExpect':slOTNConfigODUkDAPIToExpect,'slOTNConfigODUkSAPIToExpect':slOTNConfigODUkSAPIToExpect,'slOTNConfigODUkDAPIReceived':slOTNConfigODUkDAPIReceived,'slOTNConfigODUkSAPIReceived':slOTNConfigODUkSAPIReceived,'slOTNConfigOTUkTIMKillEnabled':slOTNConfigOTUkTIMKillEnabled,'slOTNConfigODUkTIMKillEnabled':slOTNConfigODUkTIMKillEnabled,'slOTNConfigInbandGCC':slOTNConfigInbandGCC,'slOTNMsiDisable':slOTNMsiDisable,'slOTNPm':slOTNPm,'slOTNCurrentPmTable':slOTNCurrentPmTable,'slOTNCurrentPmEntry':slOTNCurrentPmEntry,_F:slOTNCurrentPmIndex,'slOTNCurrentPmFecCe':slOTNCurrentPmFecCe,'slOTNCurrentPmFecCerMant':slOTNCurrentPmFecCerMant,'slOTNCurrentPmFecCerExp':slOTNCurrentPmFecCerExp,'slOTNCurrentPmFecCerValid':slOTNCurrentPmFecCerValid,'slOTNCurrentPmFecCerMantFE':slOTNCurrentPmFecCerMantFE,'slOTNCurrentPmFecCerExpFE':slOTNCurrentPmFecCerExpFE,'slOTNCurrentPmFecCerValidFE':slOTNCurrentPmFecCerValidFE,'slOTNCurrentPmReset':slOTNCurrentPmReset,'slOTNTraps':slOTNTraps})