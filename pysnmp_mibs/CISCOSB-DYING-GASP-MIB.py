_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlDyGsp=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,245))
if mibBuilder.loadTexts:rlDyGsp.setRevisions(('2009-11-26 00:00',))
class _RlDyGspModeConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('syslogPrimary-snmpSecondary',1),('snmpPrimary-syslogSecondary',2),('syslogPrimary-NoSecondary',3),('snmpPrimary-NoSecondary',4),('disabled',5)))
_RlDyGspModeConfig_Type.__name__=_A
_RlDyGspModeConfig_Object=MibScalar
rlDyGspModeConfig=_RlDyGspModeConfig_Object((1,3,6,1,4,1,9,6,1,101,245,1),_RlDyGspModeConfig_Type())
rlDyGspModeConfig.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlDyGspModeConfig.setStatus('current')
mibBuilder.exportSymbols('CISCOSB-DYING-GASP-MIB',**{'rlDyGsp':rlDyGsp,'rlDyGspModeConfig':rlDyGspModeConfig})