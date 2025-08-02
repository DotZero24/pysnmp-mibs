_G='optXpd10ConnConfigIngressIf'
_F='optXpdConnConfigEgressIf'
_E='optXpdConnConfigIngressIf'
_D='read-only'
_C='SL-OPT-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slOpt=ModuleIdentity((1,3,6,1,4,1,4515,1,11))
_SlOptConn_ObjectIdentity=ObjectIdentity
slOptConn=_SlOptConn_ObjectIdentity((1,3,6,1,4,1,4515,1,11,1))
_OptXpdConnConfigTable_Object=MibTable
optXpdConnConfigTable=_OptXpdConnConfigTable_Object((1,3,6,1,4,1,4515,1,11,1,1))
if mibBuilder.loadTexts:optXpdConnConfigTable.setStatus(_A)
_OptXpdConnConfigEntry_Object=MibTableRow
optXpdConnConfigEntry=_OptXpdConnConfigEntry_Object((1,3,6,1,4,1,4515,1,11,1,1,1))
optXpdConnConfigEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:optXpdConnConfigEntry.setStatus(_A)
_OptXpdConnConfigIngressIf_Type=InterfaceIndex
_OptXpdConnConfigIngressIf_Object=MibTableColumn
optXpdConnConfigIngressIf=_OptXpdConnConfigIngressIf_Object((1,3,6,1,4,1,4515,1,11,1,1,1,1),_OptXpdConnConfigIngressIf_Type())
optXpdConnConfigIngressIf.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnConfigIngressIf.setStatus(_A)
_OptXpdConnConfigEgressIf_Type=InterfaceIndex
_OptXpdConnConfigEgressIf_Object=MibTableColumn
optXpdConnConfigEgressIf=_OptXpdConnConfigEgressIf_Object((1,3,6,1,4,1,4515,1,11,1,1,1,2),_OptXpdConnConfigEgressIf_Type())
optXpdConnConfigEgressIf.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnConfigEgressIf.setStatus(_A)
_OptXpdConnConfigRateControlAdmin_Type=Integer32
_OptXpdConnConfigRateControlAdmin_Object=MibTableColumn
optXpdConnConfigRateControlAdmin=_OptXpdConnConfigRateControlAdmin_Object((1,3,6,1,4,1,4515,1,11,1,1,1,3),_OptXpdConnConfigRateControlAdmin_Type())
optXpdConnConfigRateControlAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnConfigRateControlAdmin.setStatus(_A)
_OptXpdConnConfigRateControlOper_Type=Integer32
_OptXpdConnConfigRateControlOper_Object=MibTableColumn
optXpdConnConfigRateControlOper=_OptXpdConnConfigRateControlOper_Object((1,3,6,1,4,1,4515,1,11,1,1,1,4),_OptXpdConnConfigRateControlOper_Type())
optXpdConnConfigRateControlOper.setMaxAccess(_D)
if mibBuilder.loadTexts:optXpdConnConfigRateControlOper.setStatus(_A)
_OptXpdConnConfigRowStatus_Type=RowStatus
_OptXpdConnConfigRowStatus_Object=MibTableColumn
optXpdConnConfigRowStatus=_OptXpdConnConfigRowStatus_Object((1,3,6,1,4,1,4515,1,11,1,1,1,5),_OptXpdConnConfigRowStatus_Type())
optXpdConnConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnConfigRowStatus.setStatus(_A)
_OptXpdConnConfigLosPropagation_Type=TruthValue
_OptXpdConnConfigLosPropagation_Object=MibTableColumn
optXpdConnConfigLosPropagation=_OptXpdConnConfigLosPropagation_Object((1,3,6,1,4,1,4515,1,11,1,1,1,6),_OptXpdConnConfigLosPropagation_Type())
optXpdConnConfigLosPropagation.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnConfigLosPropagation.setStatus(_A)
_OptXpdConnSonetRate_Type=TruthValue
_OptXpdConnSonetRate_Object=MibTableColumn
optXpdConnSonetRate=_OptXpdConnSonetRate_Object((1,3,6,1,4,1,4515,1,11,1,1,1,7),_OptXpdConnSonetRate_Type())
optXpdConnSonetRate.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpdConnSonetRate.setStatus(_A)
_OptXpd10ConnConfigTable_Object=MibTable
optXpd10ConnConfigTable=_OptXpd10ConnConfigTable_Object((1,3,6,1,4,1,4515,1,11,1,2))
if mibBuilder.loadTexts:optXpd10ConnConfigTable.setStatus(_A)
_OptXpd10ConnConfigEntry_Object=MibTableRow
optXpd10ConnConfigEntry=_OptXpd10ConnConfigEntry_Object((1,3,6,1,4,1,4515,1,11,1,2,1))
optXpd10ConnConfigEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:optXpd10ConnConfigEntry.setStatus(_A)
_OptXpd10ConnConfigIngressIf_Type=InterfaceIndex
_OptXpd10ConnConfigIngressIf_Object=MibTableColumn
optXpd10ConnConfigIngressIf=_OptXpd10ConnConfigIngressIf_Object((1,3,6,1,4,1,4515,1,11,1,2,1,1),_OptXpd10ConnConfigIngressIf_Type())
optXpd10ConnConfigIngressIf.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpd10ConnConfigIngressIf.setStatus(_A)
_OptXpd10ConnConfigEgressIf_Type=InterfaceIndex
_OptXpd10ConnConfigEgressIf_Object=MibTableColumn
optXpd10ConnConfigEgressIf=_OptXpd10ConnConfigEgressIf_Object((1,3,6,1,4,1,4515,1,11,1,2,1,2),_OptXpd10ConnConfigEgressIf_Type())
optXpd10ConnConfigEgressIf.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpd10ConnConfigEgressIf.setStatus(_A)
_OptXpd10ConnConfigRateControlOper_Type=Integer32
_OptXpd10ConnConfigRateControlOper_Object=MibTableColumn
optXpd10ConnConfigRateControlOper=_OptXpd10ConnConfigRateControlOper_Object((1,3,6,1,4,1,4515,1,11,1,2,1,3),_OptXpd10ConnConfigRateControlOper_Type())
optXpd10ConnConfigRateControlOper.setMaxAccess(_D)
if mibBuilder.loadTexts:optXpd10ConnConfigRateControlOper.setStatus(_A)
_OptXpd10ConnConfigLosPropagation_Type=TruthValue
_OptXpd10ConnConfigLosPropagation_Object=MibTableColumn
optXpd10ConnConfigLosPropagation=_OptXpd10ConnConfigLosPropagation_Object((1,3,6,1,4,1,4515,1,11,1,2,1,4),_OptXpd10ConnConfigLosPropagation_Type())
optXpd10ConnConfigLosPropagation.setMaxAccess(_B)
if mibBuilder.loadTexts:optXpd10ConnConfigLosPropagation.setStatus(_A)
_SlOptLastChange_ObjectIdentity=ObjectIdentity
slOptLastChange=_SlOptLastChange_ObjectIdentity((1,3,6,1,4,1,4515,1,11,6))
_OptXpdConnConfigLastChange_Type=TimeStamp
_OptXpdConnConfigLastChange_Object=MibScalar
optXpdConnConfigLastChange=_OptXpdConnConfigLastChange_Object((1,3,6,1,4,1,4515,1,11,6,1),_OptXpdConnConfigLastChange_Type())
optXpdConnConfigLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:optXpdConnConfigLastChange.setStatus(_A)
_SlOptTraps_ObjectIdentity=ObjectIdentity
slOptTraps=_SlOptTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,11,7))
optXpdConnConfigTableChange=NotificationType((1,3,6,1,4,1,4515,1,11,7,1))
if mibBuilder.loadTexts:optXpdConnConfigTableChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'slOpt':slOpt,'slOptConn':slOptConn,'optXpdConnConfigTable':optXpdConnConfigTable,'optXpdConnConfigEntry':optXpdConnConfigEntry,_E:optXpdConnConfigIngressIf,_F:optXpdConnConfigEgressIf,'optXpdConnConfigRateControlAdmin':optXpdConnConfigRateControlAdmin,'optXpdConnConfigRateControlOper':optXpdConnConfigRateControlOper,'optXpdConnConfigRowStatus':optXpdConnConfigRowStatus,'optXpdConnConfigLosPropagation':optXpdConnConfigLosPropagation,'optXpdConnSonetRate':optXpdConnSonetRate,'optXpd10ConnConfigTable':optXpd10ConnConfigTable,'optXpd10ConnConfigEntry':optXpd10ConnConfigEntry,_G:optXpd10ConnConfigIngressIf,'optXpd10ConnConfigEgressIf':optXpd10ConnConfigEgressIf,'optXpd10ConnConfigRateControlOper':optXpd10ConnConfigRateControlOper,'optXpd10ConnConfigLosPropagation':optXpd10ConnConfigLosPropagation,'slOptLastChange':slOptLastChange,'optXpdConnConfigLastChange':optXpdConnConfigLastChange,'slOptTraps':slOptTraps,'optXpdConnConfigTableChange':optXpdConnConfigTableChange})