_O='sapCircIndex'
_N='sapCircSysInstance'
_M='auto-off'
_L='auto-on'
_K='ripCircIndex'
_J='ripCircSysInstance'
_I='sapSysInstance'
_H='ripSysInstance'
_G='on'
_F='off'
_E='read-only'
_D='NOVELL-RIPSAP-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mibDoc,=mibBuilder.importSymbols('NOVELL-IPX-MIB','mibDoc')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ripsap_ObjectIdentity=ObjectIdentity
ripsap=_Ripsap_ObjectIdentity((1,3,6,1,4,1,23,2,20))
_RipsapSystem_ObjectIdentity=ObjectIdentity
ripsapSystem=_RipsapSystem_ObjectIdentity((1,3,6,1,4,1,23,2,20,1))
_RipSysTable_Object=MibTable
ripSysTable=_RipSysTable_Object((1,3,6,1,4,1,23,2,20,1,1))
if mibBuilder.loadTexts:ripSysTable.setStatus(_A)
_RipSysEntry_Object=MibTableRow
ripSysEntry=_RipSysEntry_Object((1,3,6,1,4,1,23,2,20,1,1,1))
ripSysEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:ripSysEntry.setStatus(_A)
_RipSysInstance_Type=Integer32
_RipSysInstance_Object=MibTableColumn
ripSysInstance=_RipSysInstance_Object((1,3,6,1,4,1,23,2,20,1,1,1,1),_RipSysInstance_Type())
ripSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ripSysInstance.setStatus(_A)
class _RipSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RipSysState_Type.__name__=_C
_RipSysState_Object=MibTableColumn
ripSysState=_RipSysState_Object((1,3,6,1,4,1,23,2,20,1,1,1,2),_RipSysState_Type())
ripSysState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripSysState.setStatus(_A)
_RipSysIncorrectPackets_Type=Counter32
_RipSysIncorrectPackets_Object=MibTableColumn
ripSysIncorrectPackets=_RipSysIncorrectPackets_Object((1,3,6,1,4,1,23,2,20,1,1,1,3),_RipSysIncorrectPackets_Type())
ripSysIncorrectPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ripSysIncorrectPackets.setStatus(_A)
_SapSysTable_Object=MibTable
sapSysTable=_SapSysTable_Object((1,3,6,1,4,1,23,2,20,1,2))
if mibBuilder.loadTexts:sapSysTable.setStatus(_A)
_SapSysEntry_Object=MibTableRow
sapSysEntry=_SapSysEntry_Object((1,3,6,1,4,1,23,2,20,1,2,1))
sapSysEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:sapSysEntry.setStatus(_A)
_SapSysInstance_Type=Integer32
_SapSysInstance_Object=MibTableColumn
sapSysInstance=_SapSysInstance_Object((1,3,6,1,4,1,23,2,20,1,2,1,1),_SapSysInstance_Type())
sapSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sapSysInstance.setStatus(_A)
class _SapSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SapSysState_Type.__name__=_C
_SapSysState_Object=MibTableColumn
sapSysState=_SapSysState_Object((1,3,6,1,4,1,23,2,20,1,2,1,2),_SapSysState_Type())
sapSysState.setMaxAccess(_B)
if mibBuilder.loadTexts:sapSysState.setStatus(_A)
_SapSysIncorrectPackets_Type=Counter32
_SapSysIncorrectPackets_Object=MibTableColumn
sapSysIncorrectPackets=_SapSysIncorrectPackets_Object((1,3,6,1,4,1,23,2,20,1,2,1,3),_SapSysIncorrectPackets_Type())
sapSysIncorrectPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:sapSysIncorrectPackets.setStatus(_A)
_RipsapCircuit_ObjectIdentity=ObjectIdentity
ripsapCircuit=_RipsapCircuit_ObjectIdentity((1,3,6,1,4,1,23,2,20,2))
_RipCircTable_Object=MibTable
ripCircTable=_RipCircTable_Object((1,3,6,1,4,1,23,2,20,2,1))
if mibBuilder.loadTexts:ripCircTable.setStatus(_A)
_RipCircEntry_Object=MibTableRow
ripCircEntry=_RipCircEntry_Object((1,3,6,1,4,1,23,2,20,2,1,1))
ripCircEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:ripCircEntry.setStatus(_A)
_RipCircSysInstance_Type=Integer32
_RipCircSysInstance_Object=MibTableColumn
ripCircSysInstance=_RipCircSysInstance_Object((1,3,6,1,4,1,23,2,20,2,1,1,1),_RipCircSysInstance_Type())
ripCircSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircSysInstance.setStatus(_A)
_RipCircIndex_Type=Integer32
_RipCircIndex_Object=MibTableColumn
ripCircIndex=_RipCircIndex_Object((1,3,6,1,4,1,23,2,20,2,1,1,2),_RipCircIndex_Type())
ripCircIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircIndex.setStatus(_A)
class _RipCircState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_RipCircState_Type.__name__=_C
_RipCircState_Object=MibTableColumn
ripCircState=_RipCircState_Object((1,3,6,1,4,1,23,2,20,2,1,1,3),_RipCircState_Type())
ripCircState.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircState.setStatus(_A)
_RipCircPace_Type=Integer32
_RipCircPace_Object=MibTableColumn
ripCircPace=_RipCircPace_Object((1,3,6,1,4,1,23,2,20,2,1,1,4),_RipCircPace_Type())
ripCircPace.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircPace.setStatus(_A)
class _RipCircUpdate_Type(Integer32):defaultValue=60
_RipCircUpdate_Type.__name__=_C
_RipCircUpdate_Object=MibTableColumn
ripCircUpdate=_RipCircUpdate_Object((1,3,6,1,4,1,23,2,20,2,1,1,5),_RipCircUpdate_Type())
ripCircUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircUpdate.setStatus(_A)
class _RipCircAgeMultiplier_Type(Integer32):defaultValue=4
_RipCircAgeMultiplier_Type.__name__=_C
_RipCircAgeMultiplier_Object=MibTableColumn
ripCircAgeMultiplier=_RipCircAgeMultiplier_Object((1,3,6,1,4,1,23,2,20,2,1,1,6),_RipCircAgeMultiplier_Type())
ripCircAgeMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircAgeMultiplier.setStatus(_A)
_RipCircPacketSize_Type=Integer32
_RipCircPacketSize_Object=MibTableColumn
ripCircPacketSize=_RipCircPacketSize_Object((1,3,6,1,4,1,23,2,20,2,1,1,7),_RipCircPacketSize_Type())
ripCircPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ripCircPacketSize.setStatus(_A)
_RipCircOutPackets_Type=Counter32
_RipCircOutPackets_Object=MibTableColumn
ripCircOutPackets=_RipCircOutPackets_Object((1,3,6,1,4,1,23,2,20,2,1,1,8),_RipCircOutPackets_Type())
ripCircOutPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ripCircOutPackets.setStatus(_A)
_RipCircInPackets_Type=Counter32
_RipCircInPackets_Object=MibTableColumn
ripCircInPackets=_RipCircInPackets_Object((1,3,6,1,4,1,23,2,20,2,1,1,9),_RipCircInPackets_Type())
ripCircInPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:ripCircInPackets.setStatus(_A)
_SapCircTable_Object=MibTable
sapCircTable=_SapCircTable_Object((1,3,6,1,4,1,23,2,20,2,2))
if mibBuilder.loadTexts:sapCircTable.setStatus(_A)
_SapCircEntry_Object=MibTableRow
sapCircEntry=_SapCircEntry_Object((1,3,6,1,4,1,23,2,20,2,2,1))
sapCircEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:sapCircEntry.setStatus(_A)
_SapCircSysInstance_Type=Integer32
_SapCircSysInstance_Object=MibTableColumn
sapCircSysInstance=_SapCircSysInstance_Object((1,3,6,1,4,1,23,2,20,2,2,1,1),_SapCircSysInstance_Type())
sapCircSysInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircSysInstance.setStatus(_A)
_SapCircIndex_Type=Integer32
_SapCircIndex_Object=MibTableColumn
sapCircIndex=_SapCircIndex_Object((1,3,6,1,4,1,23,2,20,2,2,1,2),_SapCircIndex_Type())
sapCircIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircIndex.setStatus(_A)
class _SapCircState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_SapCircState_Type.__name__=_C
_SapCircState_Object=MibTableColumn
sapCircState=_SapCircState_Object((1,3,6,1,4,1,23,2,20,2,2,1,3),_SapCircState_Type())
sapCircState.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircState.setStatus(_A)
_SapCircPace_Type=Integer32
_SapCircPace_Object=MibTableColumn
sapCircPace=_SapCircPace_Object((1,3,6,1,4,1,23,2,20,2,2,1,4),_SapCircPace_Type())
sapCircPace.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircPace.setStatus(_A)
class _SapCircUpdate_Type(Integer32):defaultValue=60
_SapCircUpdate_Type.__name__=_C
_SapCircUpdate_Object=MibTableColumn
sapCircUpdate=_SapCircUpdate_Object((1,3,6,1,4,1,23,2,20,2,2,1,5),_SapCircUpdate_Type())
sapCircUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircUpdate.setStatus(_A)
class _SapCircAgeMultiplier_Type(Integer32):defaultValue=4
_SapCircAgeMultiplier_Type.__name__=_C
_SapCircAgeMultiplier_Object=MibTableColumn
sapCircAgeMultiplier=_SapCircAgeMultiplier_Object((1,3,6,1,4,1,23,2,20,2,2,1,6),_SapCircAgeMultiplier_Type())
sapCircAgeMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircAgeMultiplier.setStatus(_A)
_SapCircPacketSize_Type=Integer32
_SapCircPacketSize_Object=MibTableColumn
sapCircPacketSize=_SapCircPacketSize_Object((1,3,6,1,4,1,23,2,20,2,2,1,7),_SapCircPacketSize_Type())
sapCircPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircPacketSize.setStatus(_A)
class _SapCircGetNearestServerReply_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_SapCircGetNearestServerReply_Type.__name__=_C
_SapCircGetNearestServerReply_Object=MibTableColumn
sapCircGetNearestServerReply=_SapCircGetNearestServerReply_Object((1,3,6,1,4,1,23,2,20,2,2,1,8),_SapCircGetNearestServerReply_Type())
sapCircGetNearestServerReply.setMaxAccess(_B)
if mibBuilder.loadTexts:sapCircGetNearestServerReply.setStatus(_A)
_SapCircOutPackets_Type=Counter32
_SapCircOutPackets_Object=MibTableColumn
sapCircOutPackets=_SapCircOutPackets_Object((1,3,6,1,4,1,23,2,20,2,2,1,9),_SapCircOutPackets_Type())
sapCircOutPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:sapCircOutPackets.setStatus(_A)
_SapCircInPackets_Type=Counter32
_SapCircInPackets_Object=MibTableColumn
sapCircInPackets=_SapCircInPackets_Object((1,3,6,1,4,1,23,2,20,2,2,1,10),_SapCircInPackets_Type())
sapCircInPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:sapCircInPackets.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ripsap':ripsap,'ripsapSystem':ripsapSystem,'ripSysTable':ripSysTable,'ripSysEntry':ripSysEntry,_H:ripSysInstance,'ripSysState':ripSysState,'ripSysIncorrectPackets':ripSysIncorrectPackets,'sapSysTable':sapSysTable,'sapSysEntry':sapSysEntry,_I:sapSysInstance,'sapSysState':sapSysState,'sapSysIncorrectPackets':sapSysIncorrectPackets,'ripsapCircuit':ripsapCircuit,'ripCircTable':ripCircTable,'ripCircEntry':ripCircEntry,_J:ripCircSysInstance,_K:ripCircIndex,'ripCircState':ripCircState,'ripCircPace':ripCircPace,'ripCircUpdate':ripCircUpdate,'ripCircAgeMultiplier':ripCircAgeMultiplier,'ripCircPacketSize':ripCircPacketSize,'ripCircOutPackets':ripCircOutPackets,'ripCircInPackets':ripCircInPackets,'sapCircTable':sapCircTable,'sapCircEntry':sapCircEntry,_N:sapCircSysInstance,_O:sapCircIndex,'sapCircState':sapCircState,'sapCircPace':sapCircPace,'sapCircUpdate':sapCircUpdate,'sapCircAgeMultiplier':sapCircAgeMultiplier,'sapCircPacketSize':sapCircPacketSize,'sapCircGetNearestServerReply':sapCircGetNearestServerReply,'sapCircOutPackets':sapCircOutPackets,'sapCircInPackets':sapCircInPackets})