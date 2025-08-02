if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMsataMIB=ModuleIdentity((1,3,6,1,4,1,9,9,860))
if mibBuilder.loadTexts:ciscoMsataMIB.setRevisions(('2019-01-09 00:00',))
_CiscoMsataMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMsataMIBObjects=_CiscoMsataMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,860,0))
_CiscoMsata_Type=OctetString
_CiscoMsata_Object=MibScalar
ciscoMsata=_CiscoMsata_Object((1,3,6,1,4,1,9,9,860,0,1),_CiscoMsata_Type())
ciscoMsata.setMaxAccess('read-only')
if mibBuilder.loadTexts:ciscoMsata.setStatus('current')
mibBuilder.exportSymbols('CISCO-MSATA-MIB',**{'ciscoMsataMIB':ciscoMsataMIB,'ciscoMsataMIBObjects':ciscoMsataMIBObjects,'ciscoMsata':ciscoMsata})