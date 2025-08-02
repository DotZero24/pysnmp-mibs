_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethernetOamStatistics,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamStatistics')
_EthernetOamPduStatTable_Object=MibTable
ethernetOamPduStatTable=_EthernetOamPduStatTable_Object((1,3,6,1,4,1,11863,6,60,1,6,1))
if mibBuilder.loadTexts:ethernetOamPduStatTable.setStatus(_A)
_EthernetOamPduStatEntry_Object=MibTableRow
ethernetOamPduStatEntry=_EthernetOamPduStatEntry_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1))
ethernetOamPduStatEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ethernetOamPduStatEntry.setStatus(_A)
_EthernetOamPduStatPort_Type=DisplayString
_EthernetOamPduStatPort_Object=MibTableColumn
ethernetOamPduStatPort=_EthernetOamPduStatPort_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,1),_EthernetOamPduStatPort_Type())
ethernetOamPduStatPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatPort.setStatus(_A)
class _EthernetOamPduStatClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unchanged',0),('clear',1)))
_EthernetOamPduStatClear_Type.__name__=_E
_EthernetOamPduStatClear_Object=MibTableColumn
ethernetOamPduStatClear=_EthernetOamPduStatClear_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,2),_EthernetOamPduStatClear_Type())
ethernetOamPduStatClear.setMaxAccess('read-write')
if mibBuilder.loadTexts:ethernetOamPduStatClear.setStatus(_A)
_EthernetOamPduStatInfoTx_Type=Counter32
_EthernetOamPduStatInfoTx_Object=MibTableColumn
ethernetOamPduStatInfoTx=_EthernetOamPduStatInfoTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,3),_EthernetOamPduStatInfoTx_Type())
ethernetOamPduStatInfoTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatInfoTx.setStatus(_A)
_EthernetOamPduStatInfoRx_Type=Counter32
_EthernetOamPduStatInfoRx_Object=MibTableColumn
ethernetOamPduStatInfoRx=_EthernetOamPduStatInfoRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,4),_EthernetOamPduStatInfoRx_Type())
ethernetOamPduStatInfoRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatInfoRx.setStatus(_A)
_EthernetOamPduStatUniEventTx_Type=Counter32
_EthernetOamPduStatUniEventTx_Object=MibTableColumn
ethernetOamPduStatUniEventTx=_EthernetOamPduStatUniEventTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,5),_EthernetOamPduStatUniEventTx_Type())
ethernetOamPduStatUniEventTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatUniEventTx.setStatus(_A)
_EthernetOamPduStatUniEventRx_Type=Counter32
_EthernetOamPduStatUniEventRx_Object=MibTableColumn
ethernetOamPduStatUniEventRx=_EthernetOamPduStatUniEventRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,6),_EthernetOamPduStatUniEventRx_Type())
ethernetOamPduStatUniEventRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatUniEventRx.setStatus(_A)
_EthernetOamPduStatDupEventTx_Type=Counter32
_EthernetOamPduStatDupEventTx_Object=MibTableColumn
ethernetOamPduStatDupEventTx=_EthernetOamPduStatDupEventTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,7),_EthernetOamPduStatDupEventTx_Type())
ethernetOamPduStatDupEventTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatDupEventTx.setStatus(_A)
_EthernetOamPduStatDupEventRx_Type=Counter32
_EthernetOamPduStatDupEventRx_Object=MibTableColumn
ethernetOamPduStatDupEventRx=_EthernetOamPduStatDupEventRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,8),_EthernetOamPduStatDupEventRx_Type())
ethernetOamPduStatDupEventRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatDupEventRx.setStatus(_A)
_EthernetOamPduStatVarReqTx_Type=Counter32
_EthernetOamPduStatVarReqTx_Object=MibTableColumn
ethernetOamPduStatVarReqTx=_EthernetOamPduStatVarReqTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,9),_EthernetOamPduStatVarReqTx_Type())
ethernetOamPduStatVarReqTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatVarReqTx.setStatus(_A)
_EthernetOamPduStatVarReqRx_Type=Counter32
_EthernetOamPduStatVarReqRx_Object=MibTableColumn
ethernetOamPduStatVarReqRx=_EthernetOamPduStatVarReqRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,10),_EthernetOamPduStatVarReqRx_Type())
ethernetOamPduStatVarReqRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatVarReqRx.setStatus(_A)
_EthernetOamPduStatVarRespTx_Type=Counter32
_EthernetOamPduStatVarRespTx_Object=MibTableColumn
ethernetOamPduStatVarRespTx=_EthernetOamPduStatVarRespTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,11),_EthernetOamPduStatVarRespTx_Type())
ethernetOamPduStatVarRespTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatVarRespTx.setStatus(_A)
_EthernetOamPduStatVarRespRx_Type=Counter32
_EthernetOamPduStatVarRespRx_Object=MibTableColumn
ethernetOamPduStatVarRespRx=_EthernetOamPduStatVarRespRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,12),_EthernetOamPduStatVarRespRx_Type())
ethernetOamPduStatVarRespRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatVarRespRx.setStatus(_A)
_EthernetOamPduStatLoopbackCtrlTx_Type=Counter32
_EthernetOamPduStatLoopbackCtrlTx_Object=MibTableColumn
ethernetOamPduStatLoopbackCtrlTx=_EthernetOamPduStatLoopbackCtrlTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,13),_EthernetOamPduStatLoopbackCtrlTx_Type())
ethernetOamPduStatLoopbackCtrlTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatLoopbackCtrlTx.setStatus(_A)
_EthernetOamPduStatLoopbackCtrlRx_Type=Counter32
_EthernetOamPduStatLoopbackCtrlRx_Object=MibTableColumn
ethernetOamPduStatLoopbackCtrlRx=_EthernetOamPduStatLoopbackCtrlRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,14),_EthernetOamPduStatLoopbackCtrlRx_Type())
ethernetOamPduStatLoopbackCtrlRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatLoopbackCtrlRx.setStatus(_A)
_EthernetOamPduStatOrgSpecTx_Type=Counter32
_EthernetOamPduStatOrgSpecTx_Object=MibTableColumn
ethernetOamPduStatOrgSpecTx=_EthernetOamPduStatOrgSpecTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,15),_EthernetOamPduStatOrgSpecTx_Type())
ethernetOamPduStatOrgSpecTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatOrgSpecTx.setStatus(_A)
_EthernetOamPduStatOrgSpecRx_Type=Counter32
_EthernetOamPduStatOrgSpecRx_Object=MibTableColumn
ethernetOamPduStatOrgSpecRx=_EthernetOamPduStatOrgSpecRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,16),_EthernetOamPduStatOrgSpecRx_Type())
ethernetOamPduStatOrgSpecRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatOrgSpecRx.setStatus(_A)
_EthernetOamPduStatUnsupportedTx_Type=Counter32
_EthernetOamPduStatUnsupportedTx_Object=MibTableColumn
ethernetOamPduStatUnsupportedTx=_EthernetOamPduStatUnsupportedTx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,17),_EthernetOamPduStatUnsupportedTx_Type())
ethernetOamPduStatUnsupportedTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatUnsupportedTx.setStatus(_A)
_EthernetOamPduStatUnsupportedRx_Type=Counter32
_EthernetOamPduStatUnsupportedRx_Object=MibTableColumn
ethernetOamPduStatUnsupportedRx=_EthernetOamPduStatUnsupportedRx_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,18),_EthernetOamPduStatUnsupportedRx_Type())
ethernetOamPduStatUnsupportedRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatUnsupportedRx.setStatus(_A)
_EthernetOamPduStatFrmLostDueToOam_Type=Counter32
_EthernetOamPduStatFrmLostDueToOam_Object=MibTableColumn
ethernetOamPduStatFrmLostDueToOam=_EthernetOamPduStatFrmLostDueToOam_Object((1,3,6,1,4,1,11863,6,60,1,6,1,1,19),_EthernetOamPduStatFrmLostDueToOam_Type())
ethernetOamPduStatFrmLostDueToOam.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamPduStatFrmLostDueToOam.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ETHERNETOAMPDUSTAT-MIB',**{'ethernetOamPduStatTable':ethernetOamPduStatTable,'ethernetOamPduStatEntry':ethernetOamPduStatEntry,'ethernetOamPduStatPort':ethernetOamPduStatPort,'ethernetOamPduStatClear':ethernetOamPduStatClear,'ethernetOamPduStatInfoTx':ethernetOamPduStatInfoTx,'ethernetOamPduStatInfoRx':ethernetOamPduStatInfoRx,'ethernetOamPduStatUniEventTx':ethernetOamPduStatUniEventTx,'ethernetOamPduStatUniEventRx':ethernetOamPduStatUniEventRx,'ethernetOamPduStatDupEventTx':ethernetOamPduStatDupEventTx,'ethernetOamPduStatDupEventRx':ethernetOamPduStatDupEventRx,'ethernetOamPduStatVarReqTx':ethernetOamPduStatVarReqTx,'ethernetOamPduStatVarReqRx':ethernetOamPduStatVarReqRx,'ethernetOamPduStatVarRespTx':ethernetOamPduStatVarRespTx,'ethernetOamPduStatVarRespRx':ethernetOamPduStatVarRespRx,'ethernetOamPduStatLoopbackCtrlTx':ethernetOamPduStatLoopbackCtrlTx,'ethernetOamPduStatLoopbackCtrlRx':ethernetOamPduStatLoopbackCtrlRx,'ethernetOamPduStatOrgSpecTx':ethernetOamPduStatOrgSpecTx,'ethernetOamPduStatOrgSpecRx':ethernetOamPduStatOrgSpecRx,'ethernetOamPduStatUnsupportedTx':ethernetOamPduStatUnsupportedTx,'ethernetOamPduStatUnsupportedRx':ethernetOamPduStatUnsupportedRx,'ethernetOamPduStatFrmLostDueToOam':ethernetOamPduStatFrmLostDueToOam})