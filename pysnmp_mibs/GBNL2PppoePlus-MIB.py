_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL2,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnL2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL2PppoePlus=ModuleIdentity((1,3,6,1,4,1,13464,1,2,4,6))
if mibBuilder.loadTexts:gbnL2PppoePlus.setRevisions(('1907-11-22 00:00',))
_PppoeplusOnOff_Type=TruthValue
_PppoeplusOnOff_Object=MibScalar
pppoeplusOnOff=_PppoeplusOnOff_Object((1,3,6,1,4,1,13464,1,2,4,6,1),_PppoeplusOnOff_Type())
pppoeplusOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeplusOnOff.setStatus(_C)
class _PppoeplusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standard',0),('huawei',1)))
_PppoeplusType_Type.__name__=_A
_PppoeplusType_Object=MibScalar
pppoeplusType=_PppoeplusType_Object((1,3,6,1,4,1,13464,1,2,4,6,2),_PppoeplusType_Type())
pppoeplusType.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeplusType.setStatus(_C)
mibBuilder.exportSymbols('GBNL2PppoePlus-MIB',**{'gbnL2PppoePlus':gbnL2PppoePlus,'pppoeplusOnOff':pppoeplusOnOff,'pppoeplusType':pppoeplusType})