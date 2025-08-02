_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniperUni=ModuleIdentity((1,3,6,1,4,1,4874))
if mibBuilder.loadTexts:juniperUni.setRevisions(('2003-07-30 19:03','2002-11-13 20:14','2001-06-01 21:46','2000-06-01 14:30','2000-05-24 04:00','1999-12-13 19:36','1999-11-08 00:00'))
_JuniProducts_ObjectIdentity=ObjectIdentity
juniProducts=_JuniProducts_ObjectIdentity((1,3,6,1,4,1,4874,1))
_JuniperUniMibs_ObjectIdentity=ObjectIdentity
juniperUniMibs=_JuniperUniMibs_ObjectIdentity((1,3,6,1,4,1,4874,2))
if mibBuilder.loadTexts:juniperUniMibs.setStatus(_A)
_UsVoiceMibs_ObjectIdentity=ObjectIdentity
usVoiceMibs=_UsVoiceMibs_ObjectIdentity((1,3,6,1,4,1,4874,2,1))
_JuniMibs_ObjectIdentity=ObjectIdentity
juniMibs=_JuniMibs_ObjectIdentity((1,3,6,1,4,1,4874,2,2))
_JuniperUniExperiment_ObjectIdentity=ObjectIdentity
juniperUniExperiment=_JuniperUniExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3))
if mibBuilder.loadTexts:juniperUniExperiment.setStatus(_A)
_UsVoiceExperiment_ObjectIdentity=ObjectIdentity
usVoiceExperiment=_UsVoiceExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,1))
_JuniExperiment_ObjectIdentity=ObjectIdentity
juniExperiment=_JuniExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2))
_JuniperUniAdmin_ObjectIdentity=ObjectIdentity
juniperUniAdmin=_JuniperUniAdmin_ObjectIdentity((1,3,6,1,4,1,4874,4))
if mibBuilder.loadTexts:juniperUniAdmin.setStatus(_A)
_UsVoiceAdmin_ObjectIdentity=ObjectIdentity
usVoiceAdmin=_UsVoiceAdmin_ObjectIdentity((1,3,6,1,4,1,4874,4,1))
_JuniAdmin_ObjectIdentity=ObjectIdentity
juniAdmin=_JuniAdmin_ObjectIdentity((1,3,6,1,4,1,4874,4,2))
_JuniAgentCapability_ObjectIdentity=ObjectIdentity
juniAgentCapability=_JuniAgentCapability_ObjectIdentity((1,3,6,1,4,1,4874,5))
if mibBuilder.loadTexts:juniAgentCapability.setStatus(_A)
_UsVoiceAgents_ObjectIdentity=ObjectIdentity
usVoiceAgents=_UsVoiceAgents_ObjectIdentity((1,3,6,1,4,1,4874,5,1))
_JuniAgents_ObjectIdentity=ObjectIdentity
juniAgents=_JuniAgents_ObjectIdentity((1,3,6,1,4,1,4874,5,2))
_JuniNetMgmtProducts_ObjectIdentity=ObjectIdentity
juniNetMgmtProducts=_JuniNetMgmtProducts_ObjectIdentity((1,3,6,1,4,1,4874,6))
if mibBuilder.loadTexts:juniNetMgmtProducts.setStatus(_A)
_JuniSdxMibs_ObjectIdentity=ObjectIdentity
juniSdxMibs=_JuniSdxMibs_ObjectIdentity((1,3,6,1,4,1,4874,6,1))
_JuniPibs_ObjectIdentity=ObjectIdentity
juniPibs=_JuniPibs_ObjectIdentity((1,3,6,1,4,1,4874,7))
if mibBuilder.loadTexts:juniPibs.setStatus(_A)
_JunosePibs_ObjectIdentity=ObjectIdentity
junosePibs=_JunosePibs_ObjectIdentity((1,3,6,1,4,1,4874,7,1))
if mibBuilder.loadTexts:junosePibs.setStatus(_A)
mibBuilder.exportSymbols('Juniper-UNI-SMI',**{'juniperUni':juniperUni,'juniProducts':juniProducts,'juniperUniMibs':juniperUniMibs,'usVoiceMibs':usVoiceMibs,'juniMibs':juniMibs,'juniperUniExperiment':juniperUniExperiment,'usVoiceExperiment':usVoiceExperiment,'juniExperiment':juniExperiment,'juniperUniAdmin':juniperUniAdmin,'usVoiceAdmin':usVoiceAdmin,'juniAdmin':juniAdmin,'juniAgentCapability':juniAgentCapability,'usVoiceAgents':usVoiceAgents,'juniAgents':juniAgents,'juniNetMgmtProducts':juniNetMgmtProducts,'juniSdxMibs':juniSdxMibs,'juniPibs':juniPibs,'junosePibs':junosePibs})