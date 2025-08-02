_E='pppoaCallId'
_D='BIANCA-BRICK-PPPOA-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Pppoa_ObjectIdentity=ObjectIdentity
pppoa=_Pppoa_ObjectIdentity((1,3,6,1,4,1,272,4,28))
_PppoaCallTable_Object=MibTable
pppoaCallTable=_PppoaCallTable_Object((1,3,6,1,4,1,272,4,28,1))
if mibBuilder.loadTexts:pppoaCallTable.setStatus(_A)
_PppoaCallEntry_Object=MibTableRow
pppoaCallEntry=_PppoaCallEntry_Object((1,3,6,1,4,1,272,4,28,1,1))
pppoaCallEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pppoaCallEntry.setStatus(_A)
_PppoaCallId_Type=Integer32
_PppoaCallId_Object=MibTableColumn
pppoaCallId=_PppoaCallId_Object((1,3,6,1,4,1,272,4,28,1,1,1),_PppoaCallId_Type())
pppoaCallId.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallId.setStatus(_A)
class _PppoaCallState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('established',2),('terminated',3)))
_PppoaCallState_Type.__name__=_C
_PppoaCallState_Object=MibTableColumn
pppoaCallState=_PppoaCallState_Object((1,3,6,1,4,1,272,4,28,1,1,2),_PppoaCallState_Type())
pppoaCallState.setMaxAccess('read-write')
if mibBuilder.loadTexts:pppoaCallState.setStatus(_A)
_PppoaCallReceivedPackets_Type=Counter32
_PppoaCallReceivedPackets_Object=MibTableColumn
pppoaCallReceivedPackets=_PppoaCallReceivedPackets_Object((1,3,6,1,4,1,272,4,28,1,1,3),_PppoaCallReceivedPackets_Type())
pppoaCallReceivedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallReceivedPackets.setStatus(_A)
_PppoaCallReceivedOctets_Type=Counter32
_PppoaCallReceivedOctets_Object=MibTableColumn
pppoaCallReceivedOctets=_PppoaCallReceivedOctets_Object((1,3,6,1,4,1,272,4,28,1,1,4),_PppoaCallReceivedOctets_Type())
pppoaCallReceivedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallReceivedOctets.setStatus(_A)
_PppoaCallReceivedErrors_Type=Counter32
_PppoaCallReceivedErrors_Object=MibTableColumn
pppoaCallReceivedErrors=_PppoaCallReceivedErrors_Object((1,3,6,1,4,1,272,4,28,1,1,5),_PppoaCallReceivedErrors_Type())
pppoaCallReceivedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallReceivedErrors.setStatus(_A)
_PppoaCallTransmitPackets_Type=Counter32
_PppoaCallTransmitPackets_Object=MibTableColumn
pppoaCallTransmitPackets=_PppoaCallTransmitPackets_Object((1,3,6,1,4,1,272,4,28,1,1,6),_PppoaCallTransmitPackets_Type())
pppoaCallTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallTransmitPackets.setStatus(_A)
_PppoaCallTransmitOctets_Type=Counter32
_PppoaCallTransmitOctets_Object=MibTableColumn
pppoaCallTransmitOctets=_PppoaCallTransmitOctets_Object((1,3,6,1,4,1,272,4,28,1,1,7),_PppoaCallTransmitOctets_Type())
pppoaCallTransmitOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallTransmitOctets.setStatus(_A)
_PppoaCallTransmitErrors_Type=Counter32
_PppoaCallTransmitErrors_Object=MibTableColumn
pppoaCallTransmitErrors=_PppoaCallTransmitErrors_Object((1,3,6,1,4,1,272,4,28,1,1,8),_PppoaCallTransmitErrors_Type())
pppoaCallTransmitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallTransmitErrors.setStatus(_A)
_PppoaCallInfo_Type=DisplayString
_PppoaCallInfo_Object=MibTableColumn
pppoaCallInfo=_PppoaCallInfo_Object((1,3,6,1,4,1,272,4,28,1,1,9),_PppoaCallInfo_Type())
pppoaCallInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaCallInfo.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'pppoa':pppoa,'pppoaCallTable':pppoaCallTable,'pppoaCallEntry':pppoaCallEntry,_E:pppoaCallId,'pppoaCallState':pppoaCallState,'pppoaCallReceivedPackets':pppoaCallReceivedPackets,'pppoaCallReceivedOctets':pppoaCallReceivedOctets,'pppoaCallReceivedErrors':pppoaCallReceivedErrors,'pppoaCallTransmitPackets':pppoaCallTransmitPackets,'pppoaCallTransmitOctets':pppoaCallTransmitOctets,'pppoaCallTransmitErrors':pppoaCallTransmitErrors,'pppoaCallInfo':pppoaCallInfo})