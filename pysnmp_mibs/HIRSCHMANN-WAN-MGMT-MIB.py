_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,9))
if mibBuilder.loadTexts:hmWanMgmtMib.setRevisions(('2016-08-09 00:00',))
class _HmWanMgmtAutomaticUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('triggered',2)))
_HmWanMgmtAutomaticUpdate_Type.__name__=_A
_HmWanMgmtAutomaticUpdate_Object=MibScalar
hmWanMgmtAutomaticUpdate=_HmWanMgmtAutomaticUpdate_Object((1,3,6,1,4,1,248,40,1,9,1),_HmWanMgmtAutomaticUpdate_Type())
hmWanMgmtAutomaticUpdate.setMaxAccess('read-write')
if mibBuilder.loadTexts:hmWanMgmtAutomaticUpdate.setStatus('current')
mibBuilder.exportSymbols('HIRSCHMANN-WAN-MGMT-MIB',**{'hmWanMgmtMib':hmWanMgmtMib,'hmWanMgmtAutomaticUpdate':hmWanMgmtAutomaticUpdate})