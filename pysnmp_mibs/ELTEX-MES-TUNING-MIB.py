_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesTuning=ModuleIdentity((1,3,6,1,4,1,35265,1,23,29))
if mibBuilder.loadTexts:eltMesTuning.setRevisions(('2014-12-19 00:00',))
_EltMesTcamTuning_ObjectIdentity=ObjectIdentity
eltMesTcamTuning=_EltMesTcamTuning_ObjectIdentity((1,3,6,1,4,1,35265,1,23,29,1))
_EltMaxSelectiveQinqIngressRules_Type=Integer32
_EltMaxSelectiveQinqIngressRules_Object=MibScalar
eltMaxSelectiveQinqIngressRules=_EltMaxSelectiveQinqIngressRules_Object((1,3,6,1,4,1,35265,1,23,29,1,1),_EltMaxSelectiveQinqIngressRules_Type())
eltMaxSelectiveQinqIngressRules.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMaxSelectiveQinqIngressRules.setStatus(_A)
_EltMaxSelectiveQinqIngressRulesAfterReset_Type=Integer32
_EltMaxSelectiveQinqIngressRulesAfterReset_Object=MibScalar
eltMaxSelectiveQinqIngressRulesAfterReset=_EltMaxSelectiveQinqIngressRulesAfterReset_Object((1,3,6,1,4,1,35265,1,23,29,1,2),_EltMaxSelectiveQinqIngressRulesAfterReset_Type())
eltMaxSelectiveQinqIngressRulesAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMaxSelectiveQinqIngressRulesAfterReset.setStatus(_A)
_EltMaxSelectiveQinqEgressRules_Type=Integer32
_EltMaxSelectiveQinqEgressRules_Object=MibScalar
eltMaxSelectiveQinqEgressRules=_EltMaxSelectiveQinqEgressRules_Object((1,3,6,1,4,1,35265,1,23,29,1,3),_EltMaxSelectiveQinqEgressRules_Type())
eltMaxSelectiveQinqEgressRules.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMaxSelectiveQinqEgressRules.setStatus(_A)
_EltMaxSelectiveQinqEgressRulesAfterReset_Type=Integer32
_EltMaxSelectiveQinqEgressRulesAfterReset_Object=MibScalar
eltMaxSelectiveQinqEgressRulesAfterReset=_EltMaxSelectiveQinqEgressRulesAfterReset_Object((1,3,6,1,4,1,35265,1,23,29,1,4),_EltMaxSelectiveQinqEgressRulesAfterReset_Type())
eltMaxSelectiveQinqEgressRulesAfterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMaxSelectiveQinqEgressRulesAfterReset.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-MES-TUNING-MIB',**{'eltMesTuning':eltMesTuning,'eltMesTcamTuning':eltMesTcamTuning,'eltMaxSelectiveQinqIngressRules':eltMaxSelectiveQinqIngressRules,'eltMaxSelectiveQinqIngressRulesAfterReset':eltMaxSelectiveQinqIngressRulesAfterReset,'eltMaxSelectiveQinqEgressRules':eltMaxSelectiveQinqEgressRules,'eltMaxSelectiveQinqEgressRulesAfterReset':eltMaxSelectiveQinqEgressRulesAfterReset})