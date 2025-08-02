if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adDhcpIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,80))
if mibBuilder.loadTexts:adDhcpIdentity.setRevisions(('2009-09-22 00:00',))
_AdDHCP_ObjectIdentity=ObjectIdentity
adDHCP=_AdDHCP_ObjectIdentity((1,3,6,1,4,1,664,5,80))
_AdGenDhcpClient_ObjectIdentity=ObjectIdentity
adGenDhcpClient=_AdGenDhcpClient_ObjectIdentity((1,3,6,1,4,1,664,5,80,1))
_AdGenDhcpClientId_ObjectIdentity=ObjectIdentity
adGenDhcpClientId=_AdGenDhcpClientId_ObjectIdentity((1,3,6,1,4,1,664,6,10000,80,1))
mibBuilder.exportSymbols('ADTRAN-SHARED-DHCP-MIB',**{'adDHCP':adDHCP,'adGenDhcpClient':adGenDhcpClient,'adDhcpIdentity':adDhcpIdentity,'adGenDhcpClientId':adGenDhcpClientId})