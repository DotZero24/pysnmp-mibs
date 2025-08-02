_E='current'
_D='read-write'
_C='disabled'
_B='enabled'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swRadiusAccountMGMTMIB=ModuleIdentity((1,3,6,1,4,1,171,12,55))
_RadiusAccountCtrl_ObjectIdentity=ObjectIdentity
radiusAccountCtrl=_RadiusAccountCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,55,1))
class _AccountingShellState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_AccountingShellState_Type.__name__=_A
_AccountingShellState_Object=MibScalar
accountingShellState=_AccountingShellState_Object((1,3,6,1,4,1,171,12,55,1,1),_AccountingShellState_Type())
accountingShellState.setMaxAccess(_D)
if mibBuilder.loadTexts:accountingShellState.setStatus(_E)
class _AccountingSystemState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_AccountingSystemState_Type.__name__=_A
_AccountingSystemState_Object=MibScalar
accountingSystemState=_AccountingSystemState_Object((1,3,6,1,4,1,171,12,55,1,2),_AccountingSystemState_Type())
accountingSystemState.setMaxAccess(_D)
if mibBuilder.loadTexts:accountingSystemState.setStatus(_E)
class _AccountingNetworkState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
_AccountingNetworkState_Type.__name__=_A
_AccountingNetworkState_Object=MibScalar
accountingNetworkState=_AccountingNetworkState_Object((1,3,6,1,4,1,171,12,55,1,3),_AccountingNetworkState_Type())
accountingNetworkState.setMaxAccess(_D)
if mibBuilder.loadTexts:accountingNetworkState.setStatus(_E)
mibBuilder.exportSymbols('RADIUS-ACCOUNTING-MIB',**{'swRadiusAccountMGMTMIB':swRadiusAccountMGMTMIB,'radiusAccountCtrl':radiusAccountCtrl,'accountingShellState':accountingShellState,'accountingSystemState':accountingSystemState,'accountingNetworkState':accountingNetworkState})