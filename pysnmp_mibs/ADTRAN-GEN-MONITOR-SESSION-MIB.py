_K='adGenMonitorSessionDestifIndex'
_J='not-accessible'
_I='adGenMonitorSessionSrcifIndex'
_H='read-only'
_G='adGenMonitorSessionNum'
_F='Integer32'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-create'
_B='ADTRAN-GEN-MONITOR-SESSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenMonitorSession,adGenMonitorSessionID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenMonitorSession','adGenMonitorSessionID')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adGenMonitorSessionMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,61,1))
if mibBuilder.loadTexts:adGenMonitorSessionMIB.setRevisions(('2017-12-15 00:00',))
_AdGenMonitorSessionProv_ObjectIdentity=ObjectIdentity
adGenMonitorSessionProv=_AdGenMonitorSessionProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,61,1))
_AdGenMonitorSessionTable_Object=MibTable
adGenMonitorSessionTable=_AdGenMonitorSessionTable_Object((1,3,6,1,4,1,664,5,70,61,1,1))
if mibBuilder.loadTexts:adGenMonitorSessionTable.setStatus(_A)
_AdGenMonitorSessionEntry_Object=MibTableRow
adGenMonitorSessionEntry=_AdGenMonitorSessionEntry_Object((1,3,6,1,4,1,664,5,70,61,1,1,1))
adGenMonitorSessionEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:adGenMonitorSessionEntry.setStatus(_A)
class _AdGenMonitorSessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AdGenMonitorSessionNum_Type.__name__=_F
_AdGenMonitorSessionNum_Object=MibTableColumn
adGenMonitorSessionNum=_AdGenMonitorSessionNum_Object((1,3,6,1,4,1,664,5,70,61,1,1,1,1),_AdGenMonitorSessionNum_Type())
adGenMonitorSessionNum.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenMonitorSessionNum.setStatus(_A)
class _AdGenMonitorSessionAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AdGenMonitorSessionAdminState_Type.__name__=_F
_AdGenMonitorSessionAdminState_Object=MibTableColumn
adGenMonitorSessionAdminState=_AdGenMonitorSessionAdminState_Object((1,3,6,1,4,1,664,5,70,61,1,1,1,2),_AdGenMonitorSessionAdminState_Type())
adGenMonitorSessionAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenMonitorSessionAdminState.setStatus(_A)
_AdGenMonitorSessionLastError_Type=DisplayString
_AdGenMonitorSessionLastError_Object=MibTableColumn
adGenMonitorSessionLastError=_AdGenMonitorSessionLastError_Object((1,3,6,1,4,1,664,5,70,61,1,1,1,3),_AdGenMonitorSessionLastError_Type())
adGenMonitorSessionLastError.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenMonitorSessionLastError.setStatus(_A)
_AdGenMonitorSessionRowStatus_Type=RowStatus
_AdGenMonitorSessionRowStatus_Object=MibTableColumn
adGenMonitorSessionRowStatus=_AdGenMonitorSessionRowStatus_Object((1,3,6,1,4,1,664,5,70,61,1,1,1,4),_AdGenMonitorSessionRowStatus_Type())
adGenMonitorSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenMonitorSessionRowStatus.setStatus(_A)
_AdGenMonitorSessionSrcProvTable_Object=MibTable
adGenMonitorSessionSrcProvTable=_AdGenMonitorSessionSrcProvTable_Object((1,3,6,1,4,1,664,5,70,61,1,2))
if mibBuilder.loadTexts:adGenMonitorSessionSrcProvTable.setStatus(_A)
_AdGenMonitorSessionSrcProvEntry_Object=MibTableRow
adGenMonitorSessionSrcProvEntry=_AdGenMonitorSessionSrcProvEntry_Object((1,3,6,1,4,1,664,5,70,61,1,2,1))
adGenMonitorSessionSrcProvEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:adGenMonitorSessionSrcProvEntry.setStatus(_A)
_AdGenMonitorSessionSrcifIndex_Type=InterfaceIndex
_AdGenMonitorSessionSrcifIndex_Object=MibTableColumn
adGenMonitorSessionSrcifIndex=_AdGenMonitorSessionSrcifIndex_Object((1,3,6,1,4,1,664,5,70,61,1,2,1,1),_AdGenMonitorSessionSrcifIndex_Type())
adGenMonitorSessionSrcifIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenMonitorSessionSrcifIndex.setStatus(_A)
class _AdGenMonitorSessionSrcDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rx',0),('tx',1),('both',2)))
_AdGenMonitorSessionSrcDirection_Type.__name__=_F
_AdGenMonitorSessionSrcDirection_Object=MibTableColumn
adGenMonitorSessionSrcDirection=_AdGenMonitorSessionSrcDirection_Object((1,3,6,1,4,1,664,5,70,61,1,2,1,2),_AdGenMonitorSessionSrcDirection_Type())
adGenMonitorSessionSrcDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenMonitorSessionSrcDirection.setStatus(_A)
_AdGenMonitorSessionSrcLastError_Type=DisplayString
_AdGenMonitorSessionSrcLastError_Object=MibTableColumn
adGenMonitorSessionSrcLastError=_AdGenMonitorSessionSrcLastError_Object((1,3,6,1,4,1,664,5,70,61,1,2,1,3),_AdGenMonitorSessionSrcLastError_Type())
adGenMonitorSessionSrcLastError.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenMonitorSessionSrcLastError.setStatus(_A)
_AdGenMonitorSessionSrcRowStatus_Type=RowStatus
_AdGenMonitorSessionSrcRowStatus_Object=MibTableColumn
adGenMonitorSessionSrcRowStatus=_AdGenMonitorSessionSrcRowStatus_Object((1,3,6,1,4,1,664,5,70,61,1,2,1,4),_AdGenMonitorSessionSrcRowStatus_Type())
adGenMonitorSessionSrcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenMonitorSessionSrcRowStatus.setStatus(_A)
_AdGenMonitorSessionDestProvTable_Object=MibTable
adGenMonitorSessionDestProvTable=_AdGenMonitorSessionDestProvTable_Object((1,3,6,1,4,1,664,5,70,61,1,3))
if mibBuilder.loadTexts:adGenMonitorSessionDestProvTable.setStatus(_A)
_AdGenMonitorSessionDestProvEntry_Object=MibTableRow
adGenMonitorSessionDestProvEntry=_AdGenMonitorSessionDestProvEntry_Object((1,3,6,1,4,1,664,5,70,61,1,3,1))
adGenMonitorSessionDestProvEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:adGenMonitorSessionDestProvEntry.setStatus(_A)
_AdGenMonitorSessionDestifIndex_Type=InterfaceIndex
_AdGenMonitorSessionDestifIndex_Object=MibTableColumn
adGenMonitorSessionDestifIndex=_AdGenMonitorSessionDestifIndex_Object((1,3,6,1,4,1,664,5,70,61,1,3,1,1),_AdGenMonitorSessionDestifIndex_Type())
adGenMonitorSessionDestifIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenMonitorSessionDestifIndex.setStatus(_A)
_AdGenMonitorSessionDestLastError_Type=DisplayString
_AdGenMonitorSessionDestLastError_Object=MibTableColumn
adGenMonitorSessionDestLastError=_AdGenMonitorSessionDestLastError_Object((1,3,6,1,4,1,664,5,70,61,1,3,1,2),_AdGenMonitorSessionDestLastError_Type())
adGenMonitorSessionDestLastError.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenMonitorSessionDestLastError.setStatus(_A)
_AdGenMonitorSessionDestRowStatus_Type=RowStatus
_AdGenMonitorSessionDestRowStatus_Object=MibTableColumn
adGenMonitorSessionDestRowStatus=_AdGenMonitorSessionDestRowStatus_Object((1,3,6,1,4,1,664,5,70,61,1,3,1,3),_AdGenMonitorSessionDestRowStatus_Type())
adGenMonitorSessionDestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenMonitorSessionDestRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenMonitorSessionProv':adGenMonitorSessionProv,'adGenMonitorSessionTable':adGenMonitorSessionTable,'adGenMonitorSessionEntry':adGenMonitorSessionEntry,_G:adGenMonitorSessionNum,'adGenMonitorSessionAdminState':adGenMonitorSessionAdminState,'adGenMonitorSessionLastError':adGenMonitorSessionLastError,'adGenMonitorSessionRowStatus':adGenMonitorSessionRowStatus,'adGenMonitorSessionSrcProvTable':adGenMonitorSessionSrcProvTable,'adGenMonitorSessionSrcProvEntry':adGenMonitorSessionSrcProvEntry,_I:adGenMonitorSessionSrcifIndex,'adGenMonitorSessionSrcDirection':adGenMonitorSessionSrcDirection,'adGenMonitorSessionSrcLastError':adGenMonitorSessionSrcLastError,'adGenMonitorSessionSrcRowStatus':adGenMonitorSessionSrcRowStatus,'adGenMonitorSessionDestProvTable':adGenMonitorSessionDestProvTable,'adGenMonitorSessionDestProvEntry':adGenMonitorSessionDestProvEntry,_K:adGenMonitorSessionDestifIndex,'adGenMonitorSessionDestLastError':adGenMonitorSessionDestLastError,'adGenMonitorSessionDestRowStatus':adGenMonitorSessionDestRowStatus,'adGenMonitorSessionMIB':adGenMonitorSessionMIB})