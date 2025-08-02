if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ironPort=ModuleIdentity((1,3,6,1,4,1,15497))
if mibBuilder.loadTexts:ironPort.setRevisions(('2011-05-02 16:00','2005-06-17 00:00'))
_AsyncOSAppliances_ObjectIdentity=ObjectIdentity
asyncOSAppliances=_AsyncOSAppliances_ObjectIdentity((1,3,6,1,4,1,15497,1))
_AsyncOSMail_ObjectIdentity=ObjectIdentity
asyncOSMail=_AsyncOSMail_ObjectIdentity((1,3,6,1,4,1,15497,1,1))
_AsyncOSWebSecurityAppliance_ObjectIdentity=ObjectIdentity
asyncOSWebSecurityAppliance=_AsyncOSWebSecurityAppliance_ObjectIdentity((1,3,6,1,4,1,15497,1,2))
mibBuilder.exportSymbols('IRONPORT-SMI',**{'ironPort':ironPort,'asyncOSAppliances':asyncOSAppliances,'asyncOSMail':asyncOSMail,'asyncOSWebSecurityAppliance':asyncOSWebSecurityAppliance})