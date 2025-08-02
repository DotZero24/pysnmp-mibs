_D='adGenAOSDyingGaspGroup'
_C='adGenAOSDyingGaspEvent'
_B='ADTRAN-AOS-DYING-GASP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSCommon,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSCommon','adGenAOSConformance')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSDyingGaspMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,1,11))
if mibBuilder.loadTexts:adGenAOSDyingGaspMib.setRevisions(('2015-01-05 00:00',))
_AdGenAOSDyingGasp_ObjectIdentity=ObjectIdentity
adGenAOSDyingGasp=_AdGenAOSDyingGasp_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,11))
_AdGenAOSDyingGaspTrap_ObjectIdentity=ObjectIdentity
adGenAOSDyingGaspTrap=_AdGenAOSDyingGaspTrap_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,11,0))
_AdGenAOSDyingGaspConformance_ObjectIdentity=ObjectIdentity
adGenAOSDyingGaspConformance=_AdGenAOSDyingGaspConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,25))
_AdGenAOSDyingGaspGroups_ObjectIdentity=ObjectIdentity
adGenAOSDyingGaspGroups=_AdGenAOSDyingGaspGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,25,1))
_AdGenAOSDyingGaspCompliances_ObjectIdentity=ObjectIdentity
adGenAOSDyingGaspCompliances=_AdGenAOSDyingGaspCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,25,2))
adGenAOSDyingGaspEvent=NotificationType((1,3,6,1,4,1,664,5,53,1,11,0,1))
if mibBuilder.loadTexts:adGenAOSDyingGaspEvent.setStatus(_A)
adGenAOSDyingGaspGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,25,1,1))
adGenAOSDyingGaspGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:adGenAOSDyingGaspGroup.setStatus(_A)
adGenAOSDyingGaspFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,25,2,1))
adGenAOSDyingGaspFullCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:adGenAOSDyingGaspFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAOSDyingGasp':adGenAOSDyingGasp,'adGenAOSDyingGaspTrap':adGenAOSDyingGaspTrap,_C:adGenAOSDyingGaspEvent,'adGenAOSDyingGaspConformance':adGenAOSDyingGaspConformance,'adGenAOSDyingGaspGroups':adGenAOSDyingGaspGroups,_D:adGenAOSDyingGaspGroup,'adGenAOSDyingGaspCompliances':adGenAOSDyingGaspCompliances,'adGenAOSDyingGaspFullCompliance':adGenAOSDyingGaspFullCompliance,'adGenAOSDyingGaspMib':adGenAOSDyingGaspMib})