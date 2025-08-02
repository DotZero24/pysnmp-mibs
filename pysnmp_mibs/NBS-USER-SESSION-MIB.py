_F='nbsUserSessionPID'
_E='NBS-USER-SESSION-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
nbsUserSessionMib=ModuleIdentity((1,3,6,1,4,1,629,218))
_NbsUserSessionGrp_ObjectIdentity=ObjectIdentity
nbsUserSessionGrp=_NbsUserSessionGrp_ObjectIdentity((1,3,6,1,4,1,629,218,1))
if mibBuilder.loadTexts:nbsUserSessionGrp.setStatus(_A)
_NbsUserSessionTableSize_Type=Integer32
_NbsUserSessionTableSize_Object=MibScalar
nbsUserSessionTableSize=_NbsUserSessionTableSize_Object((1,3,6,1,4,1,629,218,1,1),_NbsUserSessionTableSize_Type())
nbsUserSessionTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionTableSize.setStatus(_A)
_NbsUserSessionTable_Object=MibTable
nbsUserSessionTable=_NbsUserSessionTable_Object((1,3,6,1,4,1,629,218,1,2))
if mibBuilder.loadTexts:nbsUserSessionTable.setStatus(_A)
_NbsUserSessionEntry_Object=MibTableRow
nbsUserSessionEntry=_NbsUserSessionEntry_Object((1,3,6,1,4,1,629,218,1,2,1))
nbsUserSessionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nbsUserSessionEntry.setStatus(_A)
_NbsUserSessionPID_Type=Unsigned32
_NbsUserSessionPID_Object=MibTableColumn
nbsUserSessionPID=_NbsUserSessionPID_Object((1,3,6,1,4,1,629,218,1,2,1,1),_NbsUserSessionPID_Type())
nbsUserSessionPID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsUserSessionPID.setStatus(_A)
_NbsUserSessionRowStatus_Type=RowStatus
_NbsUserSessionRowStatus_Object=MibTableColumn
nbsUserSessionRowStatus=_NbsUserSessionRowStatus_Object((1,3,6,1,4,1,629,218,1,2,1,2),_NbsUserSessionRowStatus_Type())
nbsUserSessionRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsUserSessionRowStatus.setStatus(_A)
class _NbsUserSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('runLvl',1),('bootTime',2),('newTime',3),('oldTime',4),('initProcess',5),('loginProcess',6),('userProcess',7),('deadProcess',8),('accounting',9)))
_NbsUserSessionType_Type.__name__=_D
_NbsUserSessionType_Object=MibTableColumn
nbsUserSessionType=_NbsUserSessionType_Object((1,3,6,1,4,1,629,218,1,2,1,3),_NbsUserSessionType_Type())
nbsUserSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionType.setStatus(_A)
class _NbsUserSessionLine_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsUserSessionLine_Type.__name__=_C
_NbsUserSessionLine_Object=MibTableColumn
nbsUserSessionLine=_NbsUserSessionLine_Object((1,3,6,1,4,1,629,218,1,2,1,4),_NbsUserSessionLine_Type())
nbsUserSessionLine.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionLine.setStatus(_A)
class _NbsUserSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_NbsUserSessionId_Type.__name__=_C
_NbsUserSessionId_Object=MibTableColumn
nbsUserSessionId=_NbsUserSessionId_Object((1,3,6,1,4,1,629,218,1,2,1,5),_NbsUserSessionId_Type())
nbsUserSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionId.setStatus(_A)
class _NbsUserSessionUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsUserSessionUser_Type.__name__=_C
_NbsUserSessionUser_Object=MibTableColumn
nbsUserSessionUser=_NbsUserSessionUser_Object((1,3,6,1,4,1,629,218,1,2,1,6),_NbsUserSessionUser_Type())
nbsUserSessionUser.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionUser.setStatus(_A)
class _NbsUserSessionHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsUserSessionHost_Type.__name__=_C
_NbsUserSessionHost_Object=MibTableColumn
nbsUserSessionHost=_NbsUserSessionHost_Object((1,3,6,1,4,1,629,218,1,2,1,7),_NbsUserSessionHost_Type())
nbsUserSessionHost.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionHost.setStatus(_A)
_NbsUserSessionConnectTime_Type=Unsigned32
_NbsUserSessionConnectTime_Object=MibTableColumn
nbsUserSessionConnectTime=_NbsUserSessionConnectTime_Object((1,3,6,1,4,1,629,218,1,2,1,8),_NbsUserSessionConnectTime_Type())
nbsUserSessionConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionConnectTime.setStatus(_A)
class _NbsUserSessionVia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('notSupported',0),('console',1),('ssh',2),('telnet',3),('api',4),('snmp',5),('gui',6)))
_NbsUserSessionVia_Type.__name__=_D
_NbsUserSessionVia_Object=MibTableColumn
nbsUserSessionVia=_NbsUserSessionVia_Object((1,3,6,1,4,1,629,218,1,2,1,9),_NbsUserSessionVia_Type())
nbsUserSessionVia.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsUserSessionVia.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nbsUserSessionMib':nbsUserSessionMib,'nbsUserSessionGrp':nbsUserSessionGrp,'nbsUserSessionTableSize':nbsUserSessionTableSize,'nbsUserSessionTable':nbsUserSessionTable,'nbsUserSessionEntry':nbsUserSessionEntry,_F:nbsUserSessionPID,'nbsUserSessionRowStatus':nbsUserSessionRowStatus,'nbsUserSessionType':nbsUserSessionType,'nbsUserSessionLine':nbsUserSessionLine,'nbsUserSessionId':nbsUserSessionId,'nbsUserSessionUser':nbsUserSessionUser,'nbsUserSessionHost':nbsUserSessionHost,'nbsUserSessionConnectTime':nbsUserSessionConnectTime,'nbsUserSessionVia':nbsUserSessionVia})