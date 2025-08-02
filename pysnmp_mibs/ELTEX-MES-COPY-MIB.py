_G='eltCopyBackupHistoryIndex'
_F='ELTEX-MES-COPY-MIB'
_E='EltCopyUserBackupStatus'
_D='Integer32'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesCopy,=mibBuilder.importSymbols('ELTEX-MES','eltMesCopy')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
RlCopyLocationType,=mibBuilder.importSymbols('RADLAN-COPY-MIB','RlCopyLocationType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
class EltCopyUserBackupStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('starting',1),('stopped',2)))
class _EltCopyAutoBackupEnable_Type(TruthValue):defaultValue=2
_EltCopyAutoBackupEnable_Type.__name__=_C
_EltCopyAutoBackupEnable_Object=MibScalar
eltCopyAutoBackupEnable=_EltCopyAutoBackupEnable_Object((1,3,6,1,4,1,35265,1,23,3,1),_EltCopyAutoBackupEnable_Type())
eltCopyAutoBackupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyAutoBackupEnable.setStatus(_A)
_EltCopyAutoBackupTimeout_Type=Unsigned32
_EltCopyAutoBackupTimeout_Object=MibScalar
eltCopyAutoBackupTimeout=_EltCopyAutoBackupTimeout_Object((1,3,6,1,4,1,35265,1,23,3,2),_EltCopyAutoBackupTimeout_Type())
eltCopyAutoBackupTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyAutoBackupTimeout.setStatus(_A)
_EltCopyAutoBackupFilePath_Type=DisplayString
_EltCopyAutoBackupFilePath_Object=MibScalar
eltCopyAutoBackupFilePath=_EltCopyAutoBackupFilePath_Object((1,3,6,1,4,1,35265,1,23,3,3),_EltCopyAutoBackupFilePath_Type())
eltCopyAutoBackupFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyAutoBackupFilePath.setStatus(_A)
_EltCopyAutoBackupServerAddress_Type=DisplayString
_EltCopyAutoBackupServerAddress_Object=MibScalar
eltCopyAutoBackupServerAddress=_EltCopyAutoBackupServerAddress_Object((1,3,6,1,4,1,35265,1,23,3,4),_EltCopyAutoBackupServerAddress_Type())
eltCopyAutoBackupServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyAutoBackupServerAddress.setStatus(_A)
class _EltCopyAutoBackupOnWrite_Type(TruthValue):defaultValue=2
_EltCopyAutoBackupOnWrite_Type.__name__=_C
_EltCopyAutoBackupOnWrite_Object=MibScalar
eltCopyAutoBackupOnWrite=_EltCopyAutoBackupOnWrite_Object((1,3,6,1,4,1,35265,1,23,3,5),_EltCopyAutoBackupOnWrite_Type())
eltCopyAutoBackupOnWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyAutoBackupOnWrite.setStatus(_A)
class _EltCopyUserBackupStart_Type(EltCopyUserBackupStatus):defaultValue=2
_EltCopyUserBackupStart_Type.__name__=_E
_EltCopyUserBackupStart_Object=MibScalar
eltCopyUserBackupStart=_EltCopyUserBackupStart_Object((1,3,6,1,4,1,35265,1,23,3,6),_EltCopyUserBackupStart_Type())
eltCopyUserBackupStart.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyUserBackupStart.setStatus(_A)
class _EltCopyBackupHistoryEnable_Type(TruthValue):defaultValue=2
_EltCopyBackupHistoryEnable_Type.__name__=_C
_EltCopyBackupHistoryEnable_Object=MibScalar
eltCopyBackupHistoryEnable=_EltCopyBackupHistoryEnable_Object((1,3,6,1,4,1,35265,1,23,3,7),_EltCopyBackupHistoryEnable_Type())
eltCopyBackupHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryEnable.setStatus(_A)
_EltCopyBackupHistoryTable_Object=MibTable
eltCopyBackupHistoryTable=_EltCopyBackupHistoryTable_Object((1,3,6,1,4,1,35265,1,23,3,8))
if mibBuilder.loadTexts:eltCopyBackupHistoryTable.setStatus(_A)
_EltCopyBackupHistoryEntry_Object=MibTableRow
eltCopyBackupHistoryEntry=_EltCopyBackupHistoryEntry_Object((1,3,6,1,4,1,35265,1,23,3,8,1))
eltCopyBackupHistoryEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:eltCopyBackupHistoryEntry.setStatus(_A)
_EltCopyBackupHistoryIndex_Type=Integer32
_EltCopyBackupHistoryIndex_Object=MibTableColumn
eltCopyBackupHistoryIndex=_EltCopyBackupHistoryIndex_Object((1,3,6,1,4,1,35265,1,23,3,8,1,1),_EltCopyBackupHistoryIndex_Type())
eltCopyBackupHistoryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltCopyBackupHistoryIndex.setStatus(_A)
_EltCopyBackupHistoryDateTime_Type=DisplayString
_EltCopyBackupHistoryDateTime_Object=MibTableColumn
eltCopyBackupHistoryDateTime=_EltCopyBackupHistoryDateTime_Object((1,3,6,1,4,1,35265,1,23,3,8,1,2),_EltCopyBackupHistoryDateTime_Type())
eltCopyBackupHistoryDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryDateTime.setStatus(_A)
_EltCopyBackupHistoryDstLocation_Type=RlCopyLocationType
_EltCopyBackupHistoryDstLocation_Object=MibTableColumn
eltCopyBackupHistoryDstLocation=_EltCopyBackupHistoryDstLocation_Object((1,3,6,1,4,1,35265,1,23,3,8,1,3),_EltCopyBackupHistoryDstLocation_Type())
eltCopyBackupHistoryDstLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryDstLocation.setStatus(_A)
_EltCopyBackupHistoryServerAddr_Type=DisplayString
_EltCopyBackupHistoryServerAddr_Object=MibTableColumn
eltCopyBackupHistoryServerAddr=_EltCopyBackupHistoryServerAddr_Object((1,3,6,1,4,1,35265,1,23,3,8,1,4),_EltCopyBackupHistoryServerAddr_Type())
eltCopyBackupHistoryServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryServerAddr.setStatus(_A)
_EltCopyBackupHistoryFilePath_Type=DisplayString
_EltCopyBackupHistoryFilePath_Object=MibTableColumn
eltCopyBackupHistoryFilePath=_EltCopyBackupHistoryFilePath_Object((1,3,6,1,4,1,35265,1,23,3,8,1,5),_EltCopyBackupHistoryFilePath_Type())
eltCopyBackupHistoryFilePath.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryFilePath.setStatus(_A)
_EltCopyBackupHistoryStatus_Type=RowStatus
_EltCopyBackupHistoryStatus_Object=MibTableColumn
eltCopyBackupHistoryStatus=_EltCopyBackupHistoryStatus_Object((1,3,6,1,4,1,35265,1,23,3,8,1,6),_EltCopyBackupHistoryStatus_Type())
eltCopyBackupHistoryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryStatus.setStatus(_A)
class _EltCopyBackupHistoryAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('clearNow',2)))
_EltCopyBackupHistoryAction_Type.__name__=_D
_EltCopyBackupHistoryAction_Object=MibScalar
eltCopyBackupHistoryAction=_EltCopyBackupHistoryAction_Object((1,3,6,1,4,1,35265,1,23,3,9),_EltCopyBackupHistoryAction_Type())
eltCopyBackupHistoryAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCopyBackupHistoryAction.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_E:EltCopyUserBackupStatus,'eltCopyAutoBackupEnable':eltCopyAutoBackupEnable,'eltCopyAutoBackupTimeout':eltCopyAutoBackupTimeout,'eltCopyAutoBackupFilePath':eltCopyAutoBackupFilePath,'eltCopyAutoBackupServerAddress':eltCopyAutoBackupServerAddress,'eltCopyAutoBackupOnWrite':eltCopyAutoBackupOnWrite,'eltCopyUserBackupStart':eltCopyUserBackupStart,'eltCopyBackupHistoryEnable':eltCopyBackupHistoryEnable,'eltCopyBackupHistoryTable':eltCopyBackupHistoryTable,'eltCopyBackupHistoryEntry':eltCopyBackupHistoryEntry,_G:eltCopyBackupHistoryIndex,'eltCopyBackupHistoryDateTime':eltCopyBackupHistoryDateTime,'eltCopyBackupHistoryDstLocation':eltCopyBackupHistoryDstLocation,'eltCopyBackupHistoryServerAddr':eltCopyBackupHistoryServerAddr,'eltCopyBackupHistoryFilePath':eltCopyBackupHistoryFilePath,'eltCopyBackupHistoryStatus':eltCopyBackupHistoryStatus,'eltCopyBackupHistoryAction':eltCopyBackupHistoryAction})