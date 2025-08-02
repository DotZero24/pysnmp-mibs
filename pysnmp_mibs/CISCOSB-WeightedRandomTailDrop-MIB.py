_D='current'
_C='disable'
_B='enable'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlWeightedRandomTailDrop=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,146))
if mibBuilder.loadTexts:rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))
class _RlWeightedRandomTailDropCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_B,0),(_C,1)))
_RlWeightedRandomTailDropCurrentStatus_Type.__name__=_A
_RlWeightedRandomTailDropCurrentStatus_Object=MibScalar
rlWeightedRandomTailDropCurrentStatus=_RlWeightedRandomTailDropCurrentStatus_Object((1,3,6,1,4,1,9,6,1,101,146,1),_RlWeightedRandomTailDropCurrentStatus_Type())
rlWeightedRandomTailDropCurrentStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlWeightedRandomTailDropCurrentStatus.setStatus(_D)
class _RlWeightedRandomTailDropStatusAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_B,0),(_C,1)))
_RlWeightedRandomTailDropStatusAfterReset_Type.__name__=_A
_RlWeightedRandomTailDropStatusAfterReset_Object=MibScalar
rlWeightedRandomTailDropStatusAfterReset=_RlWeightedRandomTailDropStatusAfterReset_Object((1,3,6,1,4,1,9,6,1,101,146,2),_RlWeightedRandomTailDropStatusAfterReset_Type())
rlWeightedRandomTailDropStatusAfterReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlWeightedRandomTailDropStatusAfterReset.setStatus(_D)
mibBuilder.exportSymbols('CISCOSB-WeightedRandomTailDrop-MIB',**{'rlWeightedRandomTailDrop':rlWeightedRandomTailDrop,'rlWeightedRandomTailDropCurrentStatus':rlWeightedRandomTailDropCurrentStatus,'rlWeightedRandomTailDropStatusAfterReset':rlWeightedRandomTailDropStatusAfterReset})