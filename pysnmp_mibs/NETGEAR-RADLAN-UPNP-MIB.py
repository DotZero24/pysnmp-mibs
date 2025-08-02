_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlUPnP=ModuleIdentity((1,3,6,1,4,1,4526,17,109))
if mibBuilder.loadTexts:rlUPnP.setRevisions(('2006-03-26 00:00',))
_RlUPnPUniqueDeviceName_Type=DisplayString
_RlUPnPUniqueDeviceName_Object=MibScalar
rlUPnPUniqueDeviceName=_RlUPnPUniqueDeviceName_Object((1,3,6,1,4,1,4526,17,109,1),_RlUPnPUniqueDeviceName_Type())
rlUPnPUniqueDeviceName.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlUPnPUniqueDeviceName.setStatus(_B)
class _RlUPnPEnabling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlUPnPEnabling_Type.__name__=_A
_RlUPnPEnabling_Object=MibScalar
rlUPnPEnabling=_RlUPnPEnabling_Object((1,3,6,1,4,1,4526,17,109,2),_RlUPnPEnabling_Type())
rlUPnPEnabling.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlUPnPEnabling.setStatus(_B)
mibBuilder.exportSymbols('NETGEAR-RADLAN-UPNP-MIB',**{'rlUPnP':rlUPnP,'rlUPnPUniqueDeviceName':rlUPnPUniqueDeviceName,'rlUPnPEnabling':rlUPnPEnabling})