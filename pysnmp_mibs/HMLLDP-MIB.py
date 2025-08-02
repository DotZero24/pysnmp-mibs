_I='hmLLDPStatsIfaceID'
_H='hmLLDPStatsIfaceGroupID'
_G='hmLLDPIfaceID'
_F='hmLLDPIfaceGroupID'
_E='read-write'
_D='HMLLDP-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmLLDP=ModuleIdentity((1,3,6,1,4,1,248,14,7))
if mibBuilder.loadTexts:hmLLDP.setRevisions(('2004-11-22 00:00',))
_HmLLDPConfig_ObjectIdentity=ObjectIdentity
hmLLDPConfig=_HmLLDPConfig_ObjectIdentity((1,3,6,1,4,1,248,14,7,1))
class _HmLLDPAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmLLDPAdminStatus_Type.__name__=_B
_HmLLDPAdminStatus_Object=MibScalar
hmLLDPAdminStatus=_HmLLDPAdminStatus_Object((1,3,6,1,4,1,248,14,7,1,1),_HmLLDPAdminStatus_Type())
hmLLDPAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hmLLDPAdminStatus.setStatus(_A)
_HmLLDPInterfaceTable_Object=MibTable
hmLLDPInterfaceTable=_HmLLDPInterfaceTable_Object((1,3,6,1,4,1,248,14,7,1,2))
if mibBuilder.loadTexts:hmLLDPInterfaceTable.setStatus(_A)
_HmLLDPIfEntry_Object=MibTableRow
hmLLDPIfEntry=_HmLLDPIfEntry_Object((1,3,6,1,4,1,248,14,7,1,2,1))
hmLLDPIfEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:hmLLDPIfEntry.setStatus(_A)
class _HmLLDPIfaceGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_HmLLDPIfaceGroupID_Type.__name__=_B
_HmLLDPIfaceGroupID_Object=MibTableColumn
hmLLDPIfaceGroupID=_HmLLDPIfaceGroupID_Object((1,3,6,1,4,1,248,14,7,1,2,1,1),_HmLLDPIfaceGroupID_Type())
hmLLDPIfaceGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPIfaceGroupID.setStatus(_A)
class _HmLLDPIfaceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HmLLDPIfaceID_Type.__name__=_B
_HmLLDPIfaceID_Object=MibTableColumn
hmLLDPIfaceID=_HmLLDPIfaceID_Object((1,3,6,1,4,1,248,14,7,1,2,1,2),_HmLLDPIfaceID_Type())
hmLLDPIfaceID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPIfaceID.setStatus(_A)
class _HmLLDPIfaceHirmaMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),('disabled',4)))
_HmLLDPIfaceHirmaMode_Type.__name__=_B
_HmLLDPIfaceHirmaMode_Object=MibTableColumn
hmLLDPIfaceHirmaMode=_HmLLDPIfaceHirmaMode_Object((1,3,6,1,4,1,248,14,7,1,2,1,3),_HmLLDPIfaceHirmaMode_Type())
hmLLDPIfaceHirmaMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hmLLDPIfaceHirmaMode.setStatus(_A)
class _HmLLDPIfaceFDBMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lldpOnly',1),('macOnly',2),('both',3),('autoDetect',4)))
_HmLLDPIfaceFDBMode_Type.__name__=_B
_HmLLDPIfaceFDBMode_Object=MibTableColumn
hmLLDPIfaceFDBMode=_HmLLDPIfaceFDBMode_Object((1,3,6,1,4,1,248,14,7,1,2,1,4),_HmLLDPIfaceFDBMode_Type())
hmLLDPIfaceFDBMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hmLLDPIfaceFDBMode.setStatus(_A)
class _HmLLDPIfaceMaxNeighbors_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_HmLLDPIfaceMaxNeighbors_Type.__name__=_B
_HmLLDPIfaceMaxNeighbors_Object=MibTableColumn
hmLLDPIfaceMaxNeighbors=_HmLLDPIfaceMaxNeighbors_Object((1,3,6,1,4,1,248,14,7,1,2,1,5),_HmLLDPIfaceMaxNeighbors_Type())
hmLLDPIfaceMaxNeighbors.setMaxAccess(_E)
if mibBuilder.loadTexts:hmLLDPIfaceMaxNeighbors.setStatus(_A)
_HmLLDPStatistics_ObjectIdentity=ObjectIdentity
hmLLDPStatistics=_HmLLDPStatistics_ObjectIdentity((1,3,6,1,4,1,248,14,7,2))
_HmLLDPStatsIfTable_Object=MibTable
hmLLDPStatsIfTable=_HmLLDPStatsIfTable_Object((1,3,6,1,4,1,248,14,7,2,1))
if mibBuilder.loadTexts:hmLLDPStatsIfTable.setStatus(_A)
_HmLLDPStatsIfEntry_Object=MibTableRow
hmLLDPStatsIfEntry=_HmLLDPStatsIfEntry_Object((1,3,6,1,4,1,248,14,7,2,1,1))
hmLLDPStatsIfEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:hmLLDPStatsIfEntry.setStatus(_A)
class _HmLLDPStatsIfaceGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_HmLLDPStatsIfaceGroupID_Type.__name__=_B
_HmLLDPStatsIfaceGroupID_Object=MibTableColumn
hmLLDPStatsIfaceGroupID=_HmLLDPStatsIfaceGroupID_Object((1,3,6,1,4,1,248,14,7,2,1,1,1),_HmLLDPStatsIfaceGroupID_Type())
hmLLDPStatsIfaceGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceGroupID.setStatus(_A)
class _HmLLDPStatsIfaceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmLLDPStatsIfaceID_Type.__name__=_B
_HmLLDPStatsIfaceID_Object=MibTableColumn
hmLLDPStatsIfaceID=_HmLLDPStatsIfaceID_Object((1,3,6,1,4,1,248,14,7,2,1,1,2),_HmLLDPStatsIfaceID_Type())
hmLLDPStatsIfaceID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceID.setStatus(_A)
_HmLLDPStatsIfaceTotalFDBEntryCount_Type=Counter32
_HmLLDPStatsIfaceTotalFDBEntryCount_Object=MibTableColumn
hmLLDPStatsIfaceTotalFDBEntryCount=_HmLLDPStatsIfaceTotalFDBEntryCount_Object((1,3,6,1,4,1,248,14,7,2,1,1,3),_HmLLDPStatsIfaceTotalFDBEntryCount_Type())
hmLLDPStatsIfaceTotalFDBEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceTotalFDBEntryCount.setStatus(_A)
_HmLLDPStatsIfaceTotalEntryCount_Type=Counter32
_HmLLDPStatsIfaceTotalEntryCount_Object=MibTableColumn
hmLLDPStatsIfaceTotalEntryCount=_HmLLDPStatsIfaceTotalEntryCount_Object((1,3,6,1,4,1,248,14,7,2,1,1,4),_HmLLDPStatsIfaceTotalEntryCount_Type())
hmLLDPStatsIfaceTotalEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceTotalEntryCount.setStatus(_A)
_HmLLDPStatsIfaceIEEEEntryCount_Type=Counter32
_HmLLDPStatsIfaceIEEEEntryCount_Object=MibTableColumn
hmLLDPStatsIfaceIEEEEntryCount=_HmLLDPStatsIfaceIEEEEntryCount_Object((1,3,6,1,4,1,248,14,7,2,1,1,5),_HmLLDPStatsIfaceIEEEEntryCount_Type())
hmLLDPStatsIfaceIEEEEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceIEEEEntryCount.setStatus(_A)
_HmLLDPStatsIfaceHirmaEntryCount_Type=Counter32
_HmLLDPStatsIfaceHirmaEntryCount_Object=MibTableColumn
hmLLDPStatsIfaceHirmaEntryCount=_HmLLDPStatsIfaceHirmaEntryCount_Object((1,3,6,1,4,1,248,14,7,2,1,1,6),_HmLLDPStatsIfaceHirmaEntryCount_Type())
hmLLDPStatsIfaceHirmaEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceHirmaEntryCount.setStatus(_A)
_HmLLDPStatsIfaceFDBEntryCount_Type=Counter32
_HmLLDPStatsIfaceFDBEntryCount_Object=MibTableColumn
hmLLDPStatsIfaceFDBEntryCount=_HmLLDPStatsIfaceFDBEntryCount_Object((1,3,6,1,4,1,248,14,7,2,1,1,7),_HmLLDPStatsIfaceFDBEntryCount_Type())
hmLLDPStatsIfaceFDBEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmLLDPStatsIfaceFDBEntryCount.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hmLLDP':hmLLDP,'hmLLDPConfig':hmLLDPConfig,'hmLLDPAdminStatus':hmLLDPAdminStatus,'hmLLDPInterfaceTable':hmLLDPInterfaceTable,'hmLLDPIfEntry':hmLLDPIfEntry,_F:hmLLDPIfaceGroupID,_G:hmLLDPIfaceID,'hmLLDPIfaceHirmaMode':hmLLDPIfaceHirmaMode,'hmLLDPIfaceFDBMode':hmLLDPIfaceFDBMode,'hmLLDPIfaceMaxNeighbors':hmLLDPIfaceMaxNeighbors,'hmLLDPStatistics':hmLLDPStatistics,'hmLLDPStatsIfTable':hmLLDPStatsIfTable,'hmLLDPStatsIfEntry':hmLLDPStatsIfEntry,_H:hmLLDPStatsIfaceGroupID,_I:hmLLDPStatsIfaceID,'hmLLDPStatsIfaceTotalFDBEntryCount':hmLLDPStatsIfaceTotalFDBEntryCount,'hmLLDPStatsIfaceTotalEntryCount':hmLLDPStatsIfaceTotalEntryCount,'hmLLDPStatsIfaceIEEEEntryCount':hmLLDPStatsIfaceIEEEEntryCount,'hmLLDPStatsIfaceHirmaEntryCount':hmLLDPStatsIfaceHirmaEntryCount,'hmLLDPStatsIfaceFDBEntryCount':hmLLDPStatsIfaceFDBEntryCount})