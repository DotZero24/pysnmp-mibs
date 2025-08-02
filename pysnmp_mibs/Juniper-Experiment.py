_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniperUniExperiment,=mibBuilder.importSymbols('Juniper-UNI-SMI','juniperUniExperiment')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniExperiment=ModuleIdentity((1,3,6,1,4,1,4874,3,2))
if mibBuilder.loadTexts:juniExperiment.setRevisions(('2002-11-13 20:58','2001-06-20 20:36','2000-10-24 21:00'))
_JuniDvmrpExperiment_ObjectIdentity=ObjectIdentity
juniDvmrpExperiment=_JuniDvmrpExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1))
if mibBuilder.loadTexts:juniDvmrpExperiment.setStatus(_A)
_JuniSonetApsExperiment_ObjectIdentity=ObjectIdentity
juniSonetApsExperiment=_JuniSonetApsExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2))
if mibBuilder.loadTexts:juniSonetApsExperiment.setStatus(_A)
_JuniMplsExperiment_ObjectIdentity=ObjectIdentity
juniMplsExperiment=_JuniMplsExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2,3))
if mibBuilder.loadTexts:juniMplsExperiment.setStatus(_A)
_JuniMplsVPNExperiment_ObjectIdentity=ObjectIdentity
juniMplsVPNExperiment=_JuniMplsVPNExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2,4))
if mibBuilder.loadTexts:juniMplsVPNExperiment.setStatus(_A)
_JuniBFDExperiment_ObjectIdentity=ObjectIdentity
juniBFDExperiment=_JuniBFDExperiment_ObjectIdentity((1,3,6,1,4,1,4874,3,2,5))
if mibBuilder.loadTexts:juniBFDExperiment.setStatus(_A)
mibBuilder.exportSymbols('Juniper-Experiment',**{'juniExperiment':juniExperiment,'juniDvmrpExperiment':juniDvmrpExperiment,'juniSonetApsExperiment':juniSonetApsExperiment,'juniMplsExperiment':juniMplsExperiment,'juniMplsVPNExperiment':juniMplsVPNExperiment,'juniBFDExperiment':juniBFDExperiment})