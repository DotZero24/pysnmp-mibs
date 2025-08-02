_D='current'
_C='disable'
_B='enable'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlJumboFrames=ModuleIdentity((1,3,6,1,4,1,89,91))
if mibBuilder.loadTexts:rlJumboFrames.setRevisions(('2007-01-02 00:00',))
class _RlJumboFramesCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_RlJumboFramesCurrentStatus_Type.__name__=_A
_RlJumboFramesCurrentStatus_Object=MibScalar
rlJumboFramesCurrentStatus=_RlJumboFramesCurrentStatus_Object((1,3,6,1,4,1,89,91,1),_RlJumboFramesCurrentStatus_Type())
rlJumboFramesCurrentStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlJumboFramesCurrentStatus.setStatus(_D)
class _RlJumboFramesStatusAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_RlJumboFramesStatusAfterReset_Type.__name__=_A
_RlJumboFramesStatusAfterReset_Object=MibScalar
rlJumboFramesStatusAfterReset=_RlJumboFramesStatusAfterReset_Object((1,3,6,1,4,1,89,91,2),_RlJumboFramesStatusAfterReset_Type())
rlJumboFramesStatusAfterReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlJumboFramesStatusAfterReset.setStatus(_D)
mibBuilder.exportSymbols('RADLAN-JUMBOFRAMES-MIB',**{'rlJumboFrames':rlJumboFrames,'rlJumboFramesCurrentStatus':rlJumboFramesCurrentStatus,'rlJumboFramesStatusAfterReset':rlJumboFramesStatusAfterReset})