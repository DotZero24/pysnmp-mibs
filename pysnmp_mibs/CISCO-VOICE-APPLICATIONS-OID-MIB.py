if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoModules,=mibBuilder.importSymbols('CISCO-SMI','ciscoModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVoiceApplicationsOIDMIB=ModuleIdentity((1,3,6,1,4,1,9,12,5))
if mibBuilder.loadTexts:ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))
_CvaMIBOids_ObjectIdentity=ObjectIdentity
cvaMIBOids=_CvaMIBOids_ObjectIdentity((1,3,6,1,4,1,9,12,5,1))
_CiscoCallManager_ObjectIdentity=ObjectIdentity
ciscoCallManager=_CiscoCallManager_ObjectIdentity((1,3,6,1,4,1,9,12,5,1,1))
_CiscoCallManagerExpress_ObjectIdentity=ObjectIdentity
ciscoCallManagerExpress=_CiscoCallManagerExpress_ObjectIdentity((1,3,6,1,4,1,9,12,5,1,2))
_CiscoSRST_ObjectIdentity=ObjectIdentity
ciscoSRST=_CiscoSRST_ObjectIdentity((1,3,6,1,4,1,9,12,5,1,3))
_CiscoBTS_ObjectIdentity=ObjectIdentity
ciscoBTS=_CiscoBTS_ObjectIdentity((1,3,6,1,4,1,9,12,5,1,4))
_CiscoCSPS_ObjectIdentity=ObjectIdentity
ciscoCSPS=_CiscoCSPS_ObjectIdentity((1,3,6,1,4,1,9,12,5,1,5))
mibBuilder.exportSymbols('CISCO-VOICE-APPLICATIONS-OID-MIB',**{'ciscoVoiceApplicationsOIDMIB':ciscoVoiceApplicationsOIDMIB,'cvaMIBOids':cvaMIBOids,'ciscoCallManager':ciscoCallManager,'ciscoCallManagerExpress':ciscoCallManagerExpress,'ciscoSRST':ciscoSRST,'ciscoBTS':ciscoBTS,'ciscoCSPS':ciscoCSPS})