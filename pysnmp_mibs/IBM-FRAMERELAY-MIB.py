_J='DisplayString'
_I='IpAddress'
_H='Integer32'
_G='Gauge32'
_F='Counter32'
_E='frCircuitIfIndex'
_D='frCircuitDlci'
_C='RFC1315-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
frCircuitDlci,frCircuitIfIndex=mibBuilder.importSymbols(_C,_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_F,'Counter64',_G,_H,_I,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
Counter32,Gauge32,Integer32,IpAddress=mibBuilder.importSymbols('SNMPv2-SMI-v1',_F,_G,_H,_I)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
DisplayString,=mibBuilder.importSymbols('SNMPv2-TC-v1',_J)
_IbmIROCfrcircuit_ObjectIdentity=ObjectIdentity
ibmIROCfrcircuit=_IbmIROCfrcircuit_ObjectIdentity((1,3,6,1,4,1,2,6,119,4,4,5))
_IbmframerelayPVCTable_Object=MibTable
ibmframerelayPVCTable=_IbmframerelayPVCTable_Object((1,3,6,1,4,1,2,6,119,4,4,5,1))
if mibBuilder.loadTexts:ibmframerelayPVCTable.setStatus(_A)
_IbmframerelayPVCEntry_Object=MibTableRow
ibmframerelayPVCEntry=_IbmframerelayPVCEntry_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1))
ibmframerelayPVCEntry.setIndexNames((0,_C,_E),(0,_C,_D))
if mibBuilder.loadTexts:ibmframerelayPVCEntry.setStatus(_A)
_IbmframerelayPVCCircName_Type=DisplayString
_IbmframerelayPVCCircName_Object=MibTableColumn
ibmframerelayPVCCircName=_IbmframerelayPVCCircName_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,1),_IbmframerelayPVCCircName_Type())
ibmframerelayPVCCircName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCCircName.setStatus(_A)
_IbmframerelayPVCTimesActive_Type=Counter32
_IbmframerelayPVCTimesActive_Object=MibTableColumn
ibmframerelayPVCTimesActive=_IbmframerelayPVCTimesActive_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,2),_IbmframerelayPVCTimesActive_Type())
ibmframerelayPVCTimesActive.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCTimesActive.setStatus(_A)
_IbmframerelayPVCTimesInactive_Type=Counter32
_IbmframerelayPVCTimesInactive_Object=MibTableColumn
ibmframerelayPVCTimesInactive=_IbmframerelayPVCTimesInactive_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,3),_IbmframerelayPVCTimesInactive_Type())
ibmframerelayPVCTimesInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCTimesInactive.setStatus(_A)
_IbmframerelayPVCTimesCongested_Type=Counter32
_IbmframerelayPVCTimesCongested_Object=MibTableColumn
ibmframerelayPVCTimesCongested=_IbmframerelayPVCTimesCongested_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,4),_IbmframerelayPVCTimesCongested_Type())
ibmframerelayPVCTimesCongested.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCTimesCongested.setStatus(_A)
_IbmframerelayPVCTxQueued_Type=Gauge32
_IbmframerelayPVCTxQueued_Object=MibTableColumn
ibmframerelayPVCTxQueued=_IbmframerelayPVCTxQueued_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,5),_IbmframerelayPVCTxQueued_Type())
ibmframerelayPVCTxQueued.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCTxQueued.setStatus(_A)
_IbmframerelayPVCTxDropped_Type=Counter32
_IbmframerelayPVCTxDropped_Object=MibTableColumn
ibmframerelayPVCTxDropped=_IbmframerelayPVCTxDropped_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,6),_IbmframerelayPVCTxDropped_Type())
ibmframerelayPVCTxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmframerelayPVCTxDropped.setStatus(_A)
_IbmframerelayPVCClearAll_Type=Integer32
_IbmframerelayPVCClearAll_Object=MibTableColumn
ibmframerelayPVCClearAll=_IbmframerelayPVCClearAll_Object((1,3,6,1,4,1,2,6,119,4,4,5,1,1,7),_IbmframerelayPVCClearAll_Type())
ibmframerelayPVCClearAll.setMaxAccess('read-write')
if mibBuilder.loadTexts:ibmframerelayPVCClearAll.setStatus(_A)
mibBuilder.exportSymbols('IBM-FRAMERELAY-MIB',**{'ibmIROCfrcircuit':ibmIROCfrcircuit,'ibmframerelayPVCTable':ibmframerelayPVCTable,'ibmframerelayPVCEntry':ibmframerelayPVCEntry,'ibmframerelayPVCCircName':ibmframerelayPVCCircName,'ibmframerelayPVCTimesActive':ibmframerelayPVCTimesActive,'ibmframerelayPVCTimesInactive':ibmframerelayPVCTimesInactive,'ibmframerelayPVCTimesCongested':ibmframerelayPVCTimesCongested,'ibmframerelayPVCTxQueued':ibmframerelayPVCTxQueued,'ibmframerelayPVCTxDropped':ibmframerelayPVCTxDropped,'ibmframerelayPVCClearAll':ibmframerelayPVCClearAll})