_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dasan=ModuleIdentity((1,3,6,1,4,1,6296))
if mibBuilder.loadTexts:dasan.setRevisions(('1901-04-19 00:00',))
_DasanEvents_ObjectIdentity=ObjectIdentity
dasanEvents=_DasanEvents_ObjectIdentity((1,3,6,1,4,1,6296,0))
if mibBuilder.loadTexts:dasanEvents.setStatus(_A)
_DasanProducts_ObjectIdentity=ObjectIdentity
dasanProducts=_DasanProducts_ObjectIdentity((1,3,6,1,4,1,6296,1))
if mibBuilder.loadTexts:dasanProducts.setStatus(_A)
_Local_ObjectIdentity=ObjectIdentity
local=_Local_ObjectIdentity((1,3,6,1,4,1,6296,2))
if mibBuilder.loadTexts:local.setStatus(_A)
_Temporary_ObjectIdentity=ObjectIdentity
temporary=_Temporary_ObjectIdentity((1,3,6,1,4,1,6296,3))
if mibBuilder.loadTexts:temporary.setStatus(_A)
_Pakmon_ObjectIdentity=ObjectIdentity
pakmon=_Pakmon_ObjectIdentity((1,3,6,1,4,1,6296,4))
if mibBuilder.loadTexts:pakmon.setStatus(_A)
_Workgroup_ObjectIdentity=ObjectIdentity
workgroup=_Workgroup_ObjectIdentity((1,3,6,1,4,1,6296,5))
if mibBuilder.loadTexts:workgroup.setStatus(_A)
_OtherEnterprises_ObjectIdentity=ObjectIdentity
otherEnterprises=_OtherEnterprises_ObjectIdentity((1,3,6,1,4,1,6296,6))
if mibBuilder.loadTexts:otherEnterprises.setStatus(_A)
_DsShe_ObjectIdentity=ObjectIdentity
dsShe=_DsShe_ObjectIdentity((1,3,6,1,4,1,6296,6,2))
_DasanAgentCapability_ObjectIdentity=ObjectIdentity
dasanAgentCapability=_DasanAgentCapability_ObjectIdentity((1,3,6,1,4,1,6296,7))
if mibBuilder.loadTexts:dasanAgentCapability.setStatus(_A)
_DasanConfig_ObjectIdentity=ObjectIdentity
dasanConfig=_DasanConfig_ObjectIdentity((1,3,6,1,4,1,6296,8))
if mibBuilder.loadTexts:dasanConfig.setStatus(_A)
_DasanMgmt_ObjectIdentity=ObjectIdentity
dasanMgmt=_DasanMgmt_ObjectIdentity((1,3,6,1,4,1,6296,9))
if mibBuilder.loadTexts:dasanMgmt.setStatus(_A)
_DasanExperiment_ObjectIdentity=ObjectIdentity
dasanExperiment=_DasanExperiment_ObjectIdentity((1,3,6,1,4,1,6296,10))
if mibBuilder.loadTexts:dasanExperiment.setStatus(_A)
_DasanAdmin_ObjectIdentity=ObjectIdentity
dasanAdmin=_DasanAdmin_ObjectIdentity((1,3,6,1,4,1,6296,11))
if mibBuilder.loadTexts:dasanAdmin.setStatus(_A)
_DasanModules_ObjectIdentity=ObjectIdentity
dasanModules=_DasanModules_ObjectIdentity((1,3,6,1,4,1,6296,12))
if mibBuilder.loadTexts:dasanModules.setStatus(_A)
_Lightstream_ObjectIdentity=ObjectIdentity
lightstream=_Lightstream_ObjectIdentity((1,3,6,1,4,1,6296,13))
if mibBuilder.loadTexts:lightstream.setStatus(_A)
_Dasanworks_ObjectIdentity=ObjectIdentity
dasanworks=_Dasanworks_ObjectIdentity((1,3,6,1,4,1,6296,14))
if mibBuilder.loadTexts:dasanworks.setStatus(_A)
_Newport_ObjectIdentity=ObjectIdentity
newport=_Newport_ObjectIdentity((1,3,6,1,4,1,6296,15))
if mibBuilder.loadTexts:newport.setStatus(_A)
_DasanPartnerProducts_ObjectIdentity=ObjectIdentity
dasanPartnerProducts=_DasanPartnerProducts_ObjectIdentity((1,3,6,1,4,1,6296,16))
if mibBuilder.loadTexts:dasanPartnerProducts.setStatus(_A)
_DasanPolicy_ObjectIdentity=ObjectIdentity
dasanPolicy=_DasanPolicy_ObjectIdentity((1,3,6,1,4,1,6296,17))
if mibBuilder.loadTexts:dasanPolicy.setStatus(_A)
_SleMgmt_ObjectIdentity=ObjectIdentity
sleMgmt=_SleMgmt_ObjectIdentity((1,3,6,1,4,1,6296,101))
if mibBuilder.loadTexts:sleMgmt.setStatus(_A)
_SleV2Mgmt_ObjectIdentity=ObjectIdentity
sleV2Mgmt=_SleV2Mgmt_ObjectIdentity((1,3,6,1,4,1,6296,102))
if mibBuilder.loadTexts:sleV2Mgmt.setStatus(_A)
mibBuilder.exportSymbols('DASAN-SMI',**{'dasan':dasan,'dasanEvents':dasanEvents,'dasanProducts':dasanProducts,'local':local,'temporary':temporary,'pakmon':pakmon,'workgroup':workgroup,'otherEnterprises':otherEnterprises,'dsShe':dsShe,'dasanAgentCapability':dasanAgentCapability,'dasanConfig':dasanConfig,'dasanMgmt':dasanMgmt,'dasanExperiment':dasanExperiment,'dasanAdmin':dasanAdmin,'dasanModules':dasanModules,'lightstream':lightstream,'dasanworks':dasanworks,'newport':newport,'dasanPartnerProducts':dasanPartnerProducts,'dasanPolicy':dasanPolicy,'sleMgmt':sleMgmt,'sleV2Mgmt':sleV2Mgmt})