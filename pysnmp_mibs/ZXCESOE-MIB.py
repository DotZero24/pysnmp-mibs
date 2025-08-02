_E='zxPwIndex'
_D='ZXPW-STD-MIB'
_C='PwVlanCfg'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
zxPwCETH,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCETH')
zxPwIndex,=mibBuilder.importSymbols(_D,_E)
PwVlanCfg,=mibBuilder.importSymbols('ZXPW-TC-STD-MIB',_C)
zxCesoeMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,3,1,2))
_ZxCesoeCfgTable_Object=MibTable
zxCesoeCfgTable=_ZxCesoeCfgTable_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1))
if mibBuilder.loadTexts:zxCesoeCfgTable.setStatus(_A)
_ZxCesoeCfgEntry_Object=MibTableRow
zxCesoeCfgEntry=_ZxCesoeCfgEntry_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1))
zxCesoeCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxCesoeCfgEntry.setStatus(_A)
_ZxCesoeCfgDstMac_Type=MacAddress
_ZxCesoeCfgDstMac_Object=MibTableColumn
zxCesoeCfgDstMac=_ZxCesoeCfgDstMac_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,1),_ZxCesoeCfgDstMac_Type())
zxCesoeCfgDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgDstMac.setStatus(_A)
_ZxCesoeCfgCardIfIndex_Type=InterfaceIndexOrZero
_ZxCesoeCfgCardIfIndex_Object=MibTableColumn
zxCesoeCfgCardIfIndex=_ZxCesoeCfgCardIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,2),_ZxCesoeCfgCardIfIndex_Type())
zxCesoeCfgCardIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgCardIfIndex.setStatus(_A)
class _ZxCesoeCfgVlanId_Type(PwVlanCfg):defaultValue=1
_ZxCesoeCfgVlanId_Type.__name__=_C
_ZxCesoeCfgVlanId_Object=MibTableColumn
zxCesoeCfgVlanId=_ZxCesoeCfgVlanId_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,3),_ZxCesoeCfgVlanId_Type())
zxCesoeCfgVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgVlanId.setStatus(_A)
_ZxCesoeCfgPrio_Type=Integer32
_ZxCesoeCfgPrio_Object=MibTableColumn
zxCesoeCfgPrio=_ZxCesoeCfgPrio_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,4),_ZxCesoeCfgPrio_Type())
zxCesoeCfgPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgPrio.setStatus(_A)
_ZxCesoeCfgRowStatus_Type=RowStatus
_ZxCesoeCfgRowStatus_Object=MibTableColumn
zxCesoeCfgRowStatus=_ZxCesoeCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,5),_ZxCesoeCfgRowStatus_Type())
zxCesoeCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgRowStatus.setStatus(_A)
class _ZxCesoeCfgCVlanId_Type(PwVlanCfg):defaultValue=1
_ZxCesoeCfgCVlanId_Type.__name__=_C
_ZxCesoeCfgCVlanId_Object=MibTableColumn
zxCesoeCfgCVlanId=_ZxCesoeCfgCVlanId_Object((1,3,6,1,4,1,3902,1015,1013,3,1,2,1,1,6),_ZxCesoeCfgCVlanId_Type())
zxCesoeCfgCVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxCesoeCfgCVlanId.setStatus(_A)
mibBuilder.exportSymbols('ZXCESOE-MIB',**{'zxCesoeMIB':zxCesoeMIB,'zxCesoeCfgTable':zxCesoeCfgTable,'zxCesoeCfgEntry':zxCesoeCfgEntry,'zxCesoeCfgDstMac':zxCesoeCfgDstMac,'zxCesoeCfgCardIfIndex':zxCesoeCfgCardIfIndex,'zxCesoeCfgVlanId':zxCesoeCfgVlanId,'zxCesoeCfgPrio':zxCesoeCfgPrio,'zxCesoeCfgRowStatus':zxCesoeCfgRowStatus,'zxCesoeCfgCVlanId':zxCesoeCfgCVlanId})