_E='h3cWlanMtVcpuID'
_D='H3C-WLANMT-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cWlanMt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,157))
if mibBuilder.loadTexts:h3cWlanMt.setRevisions(('2014-09-28 17:47',))
_H3cWlanMtVCpuInfoGroup_ObjectIdentity=ObjectIdentity
h3cWlanMtVCpuInfoGroup=_H3cWlanMtVCpuInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,157,1))
_H3cWlanMtVCpuInfoTable_Object=MibTable
h3cWlanMtVCpuInfoTable=_H3cWlanMtVCpuInfoTable_Object((1,3,6,1,4,1,2011,10,2,157,1,1))
if mibBuilder.loadTexts:h3cWlanMtVCpuInfoTable.setStatus(_A)
_H3cWlanMtVCpuInfoEntry_Object=MibTableRow
h3cWlanMtVCpuInfoEntry=_H3cWlanMtVCpuInfoEntry_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1))
h3cWlanMtVCpuInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cWlanMtVCpuInfoEntry.setStatus(_A)
class _H3cWlanMtVcpuID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cWlanMtVcpuID_Type.__name__=_C
_H3cWlanMtVcpuID_Object=MibTableColumn
h3cWlanMtVcpuID=_H3cWlanMtVcpuID_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1,1),_H3cWlanMtVcpuID_Type())
h3cWlanMtVcpuID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cWlanMtVcpuID.setStatus(_A)
class _H3cWlanMtVcpuUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cWlanMtVcpuUsage_Type.__name__=_C
_H3cWlanMtVcpuUsage_Object=MibTableColumn
h3cWlanMtVcpuUsage=_H3cWlanMtVcpuUsage_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1,2),_H3cWlanMtVcpuUsage_Type())
h3cWlanMtVcpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtVcpuUsage.setStatus(_A)
_H3cWlanMtVcpuRx_Type=Counter64
_H3cWlanMtVcpuRx_Object=MibTableColumn
h3cWlanMtVcpuRx=_H3cWlanMtVcpuRx_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1,3),_H3cWlanMtVcpuRx_Type())
h3cWlanMtVcpuRx.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtVcpuRx.setStatus(_A)
_H3cWlanMtVcpuTx_Type=Counter64
_H3cWlanMtVcpuTx_Object=MibTableColumn
h3cWlanMtVcpuTx=_H3cWlanMtVcpuTx_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1,4),_H3cWlanMtVcpuTx_Type())
h3cWlanMtVcpuTx.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtVcpuTx.setStatus(_A)
_H3cWlanMtVcpuDrop_Type=Counter64
_H3cWlanMtVcpuDrop_Object=MibTableColumn
h3cWlanMtVcpuDrop=_H3cWlanMtVcpuDrop_Object((1,3,6,1,4,1,2011,10,2,157,1,1,1,5),_H3cWlanMtVcpuDrop_Type())
h3cWlanMtVcpuDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtVcpuDrop.setStatus(_A)
_H3cWlanMtFrameToCpu_ObjectIdentity=ObjectIdentity
h3cWlanMtFrameToCpu=_H3cWlanMtFrameToCpu_ObjectIdentity((1,3,6,1,4,1,2011,10,2,157,2))
_H3cWlanMtToCpuTxFrameCnt_Type=Counter64
_H3cWlanMtToCpuTxFrameCnt_Object=MibScalar
h3cWlanMtToCpuTxFrameCnt=_H3cWlanMtToCpuTxFrameCnt_Object((1,3,6,1,4,1,2011,10,2,157,2,1),_H3cWlanMtToCpuTxFrameCnt_Type())
h3cWlanMtToCpuTxFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtToCpuTxFrameCnt.setStatus(_A)
_H3cWlanMtToCpuDropFrameCnt_Type=Counter64
_H3cWlanMtToCpuDropFrameCnt_Object=MibScalar
h3cWlanMtToCpuDropFrameCnt=_H3cWlanMtToCpuDropFrameCnt_Object((1,3,6,1,4,1,2011,10,2,157,2,2),_H3cWlanMtToCpuDropFrameCnt_Type())
h3cWlanMtToCpuDropFrameCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWlanMtToCpuDropFrameCnt.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cWlanMt':h3cWlanMt,'h3cWlanMtVCpuInfoGroup':h3cWlanMtVCpuInfoGroup,'h3cWlanMtVCpuInfoTable':h3cWlanMtVCpuInfoTable,'h3cWlanMtVCpuInfoEntry':h3cWlanMtVCpuInfoEntry,_E:h3cWlanMtVcpuID,'h3cWlanMtVcpuUsage':h3cWlanMtVcpuUsage,'h3cWlanMtVcpuRx':h3cWlanMtVcpuRx,'h3cWlanMtVcpuTx':h3cWlanMtVcpuTx,'h3cWlanMtVcpuDrop':h3cWlanMtVcpuDrop,'h3cWlanMtFrameToCpu':h3cWlanMtFrameToCpu,'h3cWlanMtToCpuTxFrameCnt':h3cWlanMtToCpuTxFrameCnt,'h3cWlanMtToCpuDropFrameCnt':h3cWlanMtToCpuDropFrameCnt})