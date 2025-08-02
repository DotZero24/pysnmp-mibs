_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
nnOme40G,=mibBuilder.importSymbols('NORTEL-OME40G-MIB','nnOme40G')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nnOme40GOmCounts=ModuleIdentity((1,3,6,1,4,1,562,68,11,3,5))
if mibBuilder.loadTexts:nnOme40GOmCounts.setRevisions(('2007-02-02 00:00',))
_Generic_ObjectIdentity=ObjectIdentity
generic=_Generic_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,5,1))
_WanCountsTable_Object=MibTable
wanCountsTable=_WanCountsTable_Object((1,3,6,1,4,1,562,68,11,3,5,1,1))
if mibBuilder.loadTexts:wanCountsTable.setStatus(_A)
_WanCountsEntry_Object=MibTableRow
wanCountsEntry=_WanCountsEntry_Object((1,3,6,1,4,1,562,68,11,3,5,1,1,1))
wanCountsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:wanCountsEntry.setStatus(_A)
_WanINFRAMES_Type=Counter64
_WanINFRAMES_Object=MibTableColumn
wanINFRAMES=_WanINFRAMES_Object((1,3,6,1,4,1,562,68,11,3,5,1,1,1,1),_WanINFRAMES_Type())
wanINFRAMES.setMaxAccess(_B)
if mibBuilder.loadTexts:wanINFRAMES.setStatus(_A)
_WanINFRAMESERR_Type=Counter64
_WanINFRAMESERR_Object=MibTableColumn
wanINFRAMESERR=_WanINFRAMESERR_Object((1,3,6,1,4,1,562,68,11,3,5,1,1,1,2),_WanINFRAMESERR_Type())
wanINFRAMESERR.setMaxAccess(_B)
if mibBuilder.loadTexts:wanINFRAMESERR.setStatus(_A)
_WanINDFR_Type=Counter64
_WanINDFR_Object=MibTableColumn
wanINDFR=_WanINDFR_Object((1,3,6,1,4,1,562,68,11,3,5,1,1,1,3),_WanINDFR_Type())
wanINDFR.setMaxAccess(_B)
if mibBuilder.loadTexts:wanINDFR.setStatus(_A)
_EthCountsTable_Object=MibTable
ethCountsTable=_EthCountsTable_Object((1,3,6,1,4,1,562,68,11,3,5,1,2))
if mibBuilder.loadTexts:ethCountsTable.setStatus(_A)
_EthCountsEntry_Object=MibTableRow
ethCountsEntry=_EthCountsEntry_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1))
ethCountsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ethCountsEntry.setStatus(_A)
_EthINFRAMES_Type=Counter64
_EthINFRAMES_Object=MibTableColumn
ethINFRAMES=_EthINFRAMES_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,1),_EthINFRAMES_Type())
ethINFRAMES.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINFRAMES.setStatus(_A)
_EthINFRAMESERR_Type=Counter64
_EthINFRAMESERR_Object=MibTableColumn
ethINFRAMESERR=_EthINFRAMESERR_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,2),_EthINFRAMESERR_Type())
ethINFRAMESERR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINFRAMESERR.setStatus(_A)
_EthINDFR_Type=Counter64
_EthINDFR_Object=MibTableColumn
ethINDFR=_EthINDFR_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,3),_EthINDFR_Type())
ethINDFR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINDFR.setStatus(_A)
_EthINFRAMESDISCS_Type=Counter64
_EthINFRAMESDISCS_Object=MibTableColumn
ethINFRAMESDISCS=_EthINFRAMESDISCS_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,4),_EthINFRAMESDISCS_Type())
ethINFRAMESDISCS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINFRAMESDISCS.setStatus(_A)
_EthOUTFRAMES_Type=Counter64
_EthOUTFRAMES_Object=MibTableColumn
ethOUTFRAMES=_EthOUTFRAMES_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,5),_EthOUTFRAMES_Type())
ethOUTFRAMES.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTFRAMES.setStatus(_A)
_EthOUTFRAMESERR_Type=Counter64
_EthOUTFRAMESERR_Object=MibTableColumn
ethOUTFRAMESERR=_EthOUTFRAMESERR_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,6),_EthOUTFRAMESERR_Type())
ethOUTFRAMESERR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTFRAMESERR.setStatus(_A)
_EthINOCTETS_Type=Counter64
_EthINOCTETS_Object=MibTableColumn
ethINOCTETS=_EthINOCTETS_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,7),_EthINOCTETS_Type())
ethINOCTETS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINOCTETS.setStatus(_A)
_EthOUTOCTETS_Type=Counter64
_EthOUTOCTETS_Object=MibTableColumn
ethOUTOCTETS=_EthOUTOCTETS_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,8),_EthOUTOCTETS_Type())
ethOUTOCTETS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTOCTETS.setStatus(_A)
_EthOUTDFR_Type=Counter64
_EthOUTDFR_Object=MibTableColumn
ethOUTDFR=_EthOUTDFR_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,9),_EthOUTDFR_Type())
ethOUTDFR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTDFR.setStatus(_A)
_EthOUTFRAMESDISCDS_Type=Counter64
_EthOUTFRAMESDISCDS_Object=MibTableColumn
ethOUTFRAMESDISCDS=_EthOUTFRAMESDISCDS_Object((1,3,6,1,4,1,562,68,11,3,5,1,2,1,10),_EthOUTFRAMESDISCDS_Type())
ethOUTFRAMESDISCDS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTFRAMESDISCDS.setStatus(_A)
_Enet_ObjectIdentity=ObjectIdentity
enet=_Enet_ObjectIdentity((1,3,6,1,4,1,562,68,11,3,5,2))
_EnetCountsTable_Object=MibTable
enetCountsTable=_EnetCountsTable_Object((1,3,6,1,4,1,562,68,11,3,5,2,1))
if mibBuilder.loadTexts:enetCountsTable.setStatus(_A)
_EnetCountsEntry_Object=MibTableRow
enetCountsEntry=_EnetCountsEntry_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1))
enetCountsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:enetCountsEntry.setStatus(_A)
_EthFCSERR_Type=Counter64
_EthFCSERR_Object=MibTableColumn
ethFCSERR=_EthFCSERR_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,1),_EthFCSERR_Type())
ethFCSERR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFCSERR.setStatus(_A)
_EthJAB_Type=Counter64
_EthJAB_Object=MibTableColumn
ethJAB=_EthJAB_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,2),_EthJAB_Type())
ethJAB.setMaxAccess(_B)
if mibBuilder.loadTexts:ethJAB.setStatus(_A)
_EthFRAG_Type=Counter64
_EthFRAG_Object=MibTableColumn
ethFRAG=_EthFRAG_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,3),_EthFRAG_Type())
ethFRAG.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFRAG.setStatus(_A)
_EthFRTOOLONGS_Type=Counter64
_EthFRTOOLONGS_Object=MibTableColumn
ethFRTOOLONGS=_EthFRTOOLONGS_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,4),_EthFRTOOLONGS_Type())
ethFRTOOLONGS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFRTOOLONGS.setStatus(_A)
_EthFRTOOSHORTS_Type=Counter64
_EthFRTOOSHORTS_Object=MibTableColumn
ethFRTOOSHORTS=_EthFRTOOSHORTS_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,5),_EthFRTOOSHORTS_Type())
ethFRTOOSHORTS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFRTOOSHORTS.setStatus(_A)
_EthSYMBOLERR_Type=Counter64
_EthSYMBOLERR_Object=MibTableColumn
ethSYMBOLERR=_EthSYMBOLERR_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,6),_EthSYMBOLERR_Type())
ethSYMBOLERR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethSYMBOLERR.setStatus(_A)
_EthINPAUSEFR_Type=Counter64
_EthINPAUSEFR_Object=MibTableColumn
ethINPAUSEFR=_EthINPAUSEFR_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,7),_EthINPAUSEFR_Type())
ethINPAUSEFR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethINPAUSEFR.setStatus(_A)
_EthOUTPAUSEFR_Type=Counter64
_EthOUTPAUSEFR_Object=MibTableColumn
ethOUTPAUSEFR=_EthOUTPAUSEFR_Object((1,3,6,1,4,1,562,68,11,3,5,2,1,1,8),_EthOUTPAUSEFR_Type())
ethOUTPAUSEFR.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOUTPAUSEFR.setStatus(_A)
mibBuilder.exportSymbols('NORTEL-OME40G-OM-COUNTS-MIB',**{'nnOme40GOmCounts':nnOme40GOmCounts,'generic':generic,'wanCountsTable':wanCountsTable,'wanCountsEntry':wanCountsEntry,'wanINFRAMES':wanINFRAMES,'wanINFRAMESERR':wanINFRAMESERR,'wanINDFR':wanINDFR,'ethCountsTable':ethCountsTable,'ethCountsEntry':ethCountsEntry,'ethINFRAMES':ethINFRAMES,'ethINFRAMESERR':ethINFRAMESERR,'ethINDFR':ethINDFR,'ethINFRAMESDISCS':ethINFRAMESDISCS,'ethOUTFRAMES':ethOUTFRAMES,'ethOUTFRAMESERR':ethOUTFRAMESERR,'ethINOCTETS':ethINOCTETS,'ethOUTOCTETS':ethOUTOCTETS,'ethOUTDFR':ethOUTDFR,'ethOUTFRAMESDISCDS':ethOUTFRAMESDISCDS,'enet':enet,'enetCountsTable':enetCountsTable,'enetCountsEntry':enetCountsEntry,'ethFCSERR':ethFCSERR,'ethJAB':ethJAB,'ethFRAG':ethFRAG,'ethFRTOOLONGS':ethFRTOOLONGS,'ethFRTOOSHORTS':ethFRTOOSHORTS,'ethSYMBOLERR':ethSYMBOLERR,'ethINPAUSEFR':ethINPAUSEFR,'ethOUTPAUSEFR':ethOUTPAUSEFR})