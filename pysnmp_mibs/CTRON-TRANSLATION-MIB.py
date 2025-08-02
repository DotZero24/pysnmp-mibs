_c='fragment-if-possible'
_b='ctTransLfpsPort'
_a='ctTransOtherPort'
_Z='ctTransA2CfgPort'
_Y='ctTransIPCfgPort'
_X='ctTransNovellCfgPort'
_W='ctTransSrPort'
_V='ctTransIbmLlcPort'
_U='ctTransBcastXPort'
_T='ctTransRifDbCtrlPort'
_S='ctTransRifDbMacAddr'
_R='disable'
_Q='enable'
_P='DisplayString'
_O='ethernet802dot3Raw'
_N='ethernet802dot3'
_M='ethernetSnap'
_L='ethernetII'
_K='auto'
_J='sr'
_I='tp'
_H='CTRON-TRANSLATION-MIB'
_G='read-only'
_F='notsupported'
_E='disabled'
_D='enabled'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
ctTranslation,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctTranslation')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
_CtTransFddiAtm_ObjectIdentity=ObjectIdentity
ctTransFddiAtm=_CtTransFddiAtm_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,1))
class _CtTransFddiAtmMtu_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('greater1518MTU',1),('less1518MTU',2)))
_CtTransFddiAtmMtu_Type.__name__=_C
_CtTransFddiAtmMtu_Object=MibScalar
ctTransFddiAtmMtu=_CtTransFddiAtmMtu_Object((1,3,6,1,4,1,52,4,1,3,4,1,1),_CtTransFddiAtmMtu_Type())
ctTransFddiAtmMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiAtmMtu.setStatus(_A)
class _CtTransFddiAtmIPFrag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_CtTransFddiAtmIPFrag_Type.__name__=_C
_CtTransFddiAtmIPFrag_Object=MibScalar
ctTransFddiAtmIPFrag=_CtTransFddiAtmIPFrag_Object((1,3,6,1,4,1,52,4,1,3,4,1,2),_CtTransFddiAtmIPFrag_Type())
ctTransFddiAtmIPFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiAtmIPFrag.setStatus(_A)
_CtTransFddiEthernet_ObjectIdentity=ObjectIdentity
ctTransFddiEthernet=_CtTransFddiEthernet_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,2))
class _CtTransFddiEthernetIPFrag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransFddiEthernetIPFrag_Type.__name__=_C
_CtTransFddiEthernetIPFrag_Object=MibScalar
ctTransFddiEthernetIPFrag=_CtTransFddiEthernetIPFrag_Object((1,3,6,1,4,1,52,4,1,3,4,2,1),_CtTransFddiEthernetIPFrag_Type())
ctTransFddiEthernetIPFrag.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiEthernetIPFrag.setStatus(_A)
class _CtTransFddiSnapEthernetType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CtTransFddiSnapEthernetType_Type.__name__=_C
_CtTransFddiSnapEthernetType_Object=MibScalar
ctTransFddiSnapEthernetType=_CtTransFddiSnapEthernetType_Object((1,3,6,1,4,1,52,4,1,3,4,2,2),_CtTransFddiSnapEthernetType_Type())
ctTransFddiSnapEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiSnapEthernetType.setStatus(_A)
class _CtTransFddiEthernetAuto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('notSupported',3)))
_CtTransFddiEthernetAuto_Type.__name__=_C
_CtTransFddiEthernetAuto_Object=MibScalar
ctTransFddiEthernetAuto=_CtTransFddiEthernetAuto_Object((1,3,6,1,4,1,52,4,1,3,4,2,3),_CtTransFddiEthernetAuto_Type())
ctTransFddiEthernetAuto.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiEthernetAuto.setStatus(_A)
class _CtTransFddiEthernetSnapIPX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_CtTransFddiEthernetSnapIPX_Type.__name__=_C
_CtTransFddiEthernetSnapIPX_Object=MibScalar
ctTransFddiEthernetSnapIPX=_CtTransFddiEthernetSnapIPX_Object((1,3,6,1,4,1,52,4,1,3,4,2,4),_CtTransFddiEthernetSnapIPX_Type())
ctTransFddiEthernetSnapIPX.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiEthernetSnapIPX.setStatus(_A)
class _CtTransFddiEthernet802dot2IPX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_CtTransFddiEthernet802dot2IPX_Type.__name__=_C
_CtTransFddiEthernet802dot2IPX_Object=MibScalar
ctTransFddiEthernet802dot2IPX=_CtTransFddiEthernet802dot2IPX_Object((1,3,6,1,4,1,52,4,1,3,4,2,5),_CtTransFddiEthernet802dot2IPX_Type())
ctTransFddiEthernet802dot2IPX.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiEthernet802dot2IPX.setStatus(_A)
class _CtTransFddiEthernetMACIPX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_CtTransFddiEthernetMACIPX_Type.__name__=_C
_CtTransFddiEthernetMACIPX_Object=MibScalar
ctTransFddiEthernetMACIPX=_CtTransFddiEthernetMACIPX_Object((1,3,6,1,4,1,52,4,1,3,4,2,6),_CtTransFddiEthernetMACIPX_Type())
ctTransFddiEthernetMACIPX.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransFddiEthernetMACIPX.setStatus(_A)
_CtTransEthernetFddi_ObjectIdentity=ObjectIdentity
ctTransEthernetFddi=_CtTransEthernetFddi_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,3))
class _CtTransEthernetFddiRAW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fDDI802dot2',1),('fDDISnap',2),('fDDIMAC',3)))
_CtTransEthernetFddiRAW_Type.__name__=_C
_CtTransEthernetFddiRAW_Object=MibScalar
ctTransEthernetFddiRAW=_CtTransEthernetFddiRAW_Object((1,3,6,1,4,1,52,4,1,3,4,3,1),_CtTransEthernetFddiRAW_Type())
ctTransEthernetFddiRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransEthernetFddiRAW.setStatus(_A)
class _CtTransEthernetFddiPadVerify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('not-supported',3)))
_CtTransEthernetFddiPadVerify_Type.__name__=_C
_CtTransEthernetFddiPadVerify_Object=MibScalar
ctTransEthernetFddiPadVerify=_CtTransEthernetFddiPadVerify_Object((1,3,6,1,4,1,52,4,1,3,4,3,2),_CtTransEthernetFddiPadVerify_Type())
ctTransEthernetFddiPadVerify.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransEthernetFddiPadVerify.setStatus(_A)
_CtTransRifDb_ObjectIdentity=ObjectIdentity
ctTransRifDb=_CtTransRifDb_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,4))
_CtTransRifDbTable_Object=MibTable
ctTransRifDbTable=_CtTransRifDbTable_Object((1,3,6,1,4,1,52,4,1,3,4,4,1))
if mibBuilder.loadTexts:ctTransRifDbTable.setStatus(_A)
_CtTransRifDbEntry_Object=MibTableRow
ctTransRifDbEntry=_CtTransRifDbEntry_Object((1,3,6,1,4,1,52,4,1,3,4,4,1,1))
ctTransRifDbEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:ctTransRifDbEntry.setStatus(_A)
_CtTransRifDbMacAddr_Type=MacAddress
_CtTransRifDbMacAddr_Object=MibTableColumn
ctTransRifDbMacAddr=_CtTransRifDbMacAddr_Object((1,3,6,1,4,1,52,4,1,3,4,4,1,1,1),_CtTransRifDbMacAddr_Type())
ctTransRifDbMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransRifDbMacAddr.setStatus(_A)
_CtTransRifDbSrcPort_Type=Integer32
_CtTransRifDbSrcPort_Object=MibTableColumn
ctTransRifDbSrcPort=_CtTransRifDbSrcPort_Object((1,3,6,1,4,1,52,4,1,3,4,4,1,1,2),_CtTransRifDbSrcPort_Type())
ctTransRifDbSrcPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransRifDbSrcPort.setStatus(_A)
_CtTransRifDbLength_Type=Integer32
_CtTransRifDbLength_Object=MibTableColumn
ctTransRifDbLength=_CtTransRifDbLength_Object((1,3,6,1,4,1,52,4,1,3,4,4,1,1,3),_CtTransRifDbLength_Type())
ctTransRifDbLength.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransRifDbLength.setStatus(_A)
class _CtTransRifDbRIF_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtTransRifDbRIF_Type.__name__=_P
_CtTransRifDbRIF_Object=MibTableColumn
ctTransRifDbRIF=_CtTransRifDbRIF_Object((1,3,6,1,4,1,52,4,1,3,4,4,1,1,4),_CtTransRifDbRIF_Type())
ctTransRifDbRIF.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransRifDbRIF.setStatus(_A)
_CtTransRifDbCtrlTable_Object=MibTable
ctTransRifDbCtrlTable=_CtTransRifDbCtrlTable_Object((1,3,6,1,4,1,52,4,1,3,4,4,2))
if mibBuilder.loadTexts:ctTransRifDbCtrlTable.setStatus(_A)
_CtTransRifDbCtrlEntry_Object=MibTableRow
ctTransRifDbCtrlEntry=_CtTransRifDbCtrlEntry_Object((1,3,6,1,4,1,52,4,1,3,4,4,2,1))
ctTransRifDbCtrlEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:ctTransRifDbCtrlEntry.setStatus(_A)
_CtTransRifDbCtrlPort_Type=Integer32
_CtTransRifDbCtrlPort_Object=MibTableColumn
ctTransRifDbCtrlPort=_CtTransRifDbCtrlPort_Object((1,3,6,1,4,1,52,4,1,3,4,4,2,1,1),_CtTransRifDbCtrlPort_Type())
ctTransRifDbCtrlPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransRifDbCtrlPort.setStatus(_A)
class _CtTransRifDbWeightState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('shortestpath',2),('quickestpath',3),('largestmtu',4),('lastseen',5)))
_CtTransRifDbWeightState_Type.__name__=_C
_CtTransRifDbWeightState_Object=MibTableColumn
ctTransRifDbWeightState=_CtTransRifDbWeightState_Object((1,3,6,1,4,1,52,4,1,3,4,4,2,1,2),_CtTransRifDbWeightState_Type())
ctTransRifDbWeightState.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransRifDbWeightState.setStatus(_A)
class _CtTransRifDbCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('explorer',1),('all',2),(_F,3)))
_CtTransRifDbCtrlType_Type.__name__=_C
_CtTransRifDbCtrlType_Object=MibTableColumn
ctTransRifDbCtrlType=_CtTransRifDbCtrlType_Object((1,3,6,1,4,1,52,4,1,3,4,4,2,1,3),_CtTransRifDbCtrlType_Type())
ctTransRifDbCtrlType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransRifDbCtrlType.setStatus(_A)
_CtTransRifDbAgingTimer_Type=Integer32
_CtTransRifDbAgingTimer_Object=MibTableColumn
ctTransRifDbAgingTimer=_CtTransRifDbAgingTimer_Object((1,3,6,1,4,1,52,4,1,3,4,4,2,1,4),_CtTransRifDbAgingTimer_Type())
ctTransRifDbAgingTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransRifDbAgingTimer.setStatus(_A)
_CtTransBcastX_ObjectIdentity=ObjectIdentity
ctTransBcastX=_CtTransBcastX_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,5))
_CtTransBcastXTable_Object=MibTable
ctTransBcastXTable=_CtTransBcastXTable_Object((1,3,6,1,4,1,52,4,1,3,4,5,1))
if mibBuilder.loadTexts:ctTransBcastXTable.setStatus(_A)
_CtTransBcastXEntry_Object=MibTableRow
ctTransBcastXEntry=_CtTransBcastXEntry_Object((1,3,6,1,4,1,52,4,1,3,4,5,1,1))
ctTransBcastXEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:ctTransBcastXEntry.setStatus(_A)
_CtTransBcastXPort_Type=Integer32
_CtTransBcastXPort_Object=MibTableColumn
ctTransBcastXPort=_CtTransBcastXPort_Object((1,3,6,1,4,1,52,4,1,3,4,5,1,1,1),_CtTransBcastXPort_Type())
ctTransBcastXPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransBcastXPort.setStatus(_A)
class _CtTransBcastXMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransBcastXMode_Type.__name__=_C
_CtTransBcastXMode_Object=MibTableColumn
ctTransBcastXMode=_CtTransBcastXMode_Object((1,3,6,1,4,1,52,4,1,3,4,5,1,1,2),_CtTransBcastXMode_Type())
ctTransBcastXMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransBcastXMode.setStatus(_A)
_CtTransBcastXMedia_Type=MacAddress
_CtTransBcastXMedia_Object=MibTableColumn
ctTransBcastXMedia=_CtTransBcastXMedia_Object((1,3,6,1,4,1,52,4,1,3,4,5,1,1,3),_CtTransBcastXMedia_Type())
ctTransBcastXMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransBcastXMedia.setStatus(_A)
_CtTransBcastXCanonical_Type=MacAddress
_CtTransBcastXCanonical_Object=MibTableColumn
ctTransBcastXCanonical=_CtTransBcastXCanonical_Object((1,3,6,1,4,1,52,4,1,3,4,5,1,1,4),_CtTransBcastXCanonical_Type())
ctTransBcastXCanonical.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransBcastXCanonical.setStatus(_A)
_CtTransIbmLlc_ObjectIdentity=ObjectIdentity
ctTransIbmLlc=_CtTransIbmLlc_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,6))
_CtTransIbmLlcTable_Object=MibTable
ctTransIbmLlcTable=_CtTransIbmLlcTable_Object((1,3,6,1,4,1,52,4,1,3,4,6,1))
if mibBuilder.loadTexts:ctTransIbmLlcTable.setStatus(_A)
_CtTransIbmLlcEntry_Object=MibTableRow
ctTransIbmLlcEntry=_CtTransIbmLlcEntry_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1))
ctTransIbmLlcEntry.setIndexNames((0,_H,_V))
if mibBuilder.loadTexts:ctTransIbmLlcEntry.setStatus(_A)
_CtTransIbmLlcPort_Type=Integer32
_CtTransIbmLlcPort_Object=MibTableColumn
ctTransIbmLlcPort=_CtTransIbmLlcPort_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,1),_CtTransIbmLlcPort_Type())
ctTransIbmLlcPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransIbmLlcPort.setStatus(_A)
class _CtTransIbmLlcNullMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcNullMode_Type.__name__=_C
_CtTransIbmLlcNullMode_Object=MibTableColumn
ctTransIbmLlcNullMode=_CtTransIbmLlcNullMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,2),_CtTransIbmLlcNullMode_Type())
ctTransIbmLlcNullMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcNullMode.setStatus(_A)
class _CtTransIbmLlcSnaPathMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcSnaPathMode_Type.__name__=_C
_CtTransIbmLlcSnaPathMode_Object=MibTableColumn
ctTransIbmLlcSnaPathMode=_CtTransIbmLlcSnaPathMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,3),_CtTransIbmLlcSnaPathMode_Type())
ctTransIbmLlcSnaPathMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcSnaPathMode.setStatus(_A)
class _CtTransIbmLlcSnaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcSnaMode_Type.__name__=_C
_CtTransIbmLlcSnaMode_Object=MibTableColumn
ctTransIbmLlcSnaMode=_CtTransIbmLlcSnaMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,4),_CtTransIbmLlcSnaMode_Type())
ctTransIbmLlcSnaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcSnaMode.setStatus(_A)
class _CtTransIbmLlcNbMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcNbMode_Type.__name__=_C
_CtTransIbmLlcNbMode_Object=MibTableColumn
ctTransIbmLlcNbMode=_CtTransIbmLlcNbMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,5),_CtTransIbmLlcNbMode_Type())
ctTransIbmLlcNbMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcNbMode.setStatus(_A)
class _CtTransIbmLlcLnmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcLnmMode_Type.__name__=_C
_CtTransIbmLlcLnmMode_Object=MibTableColumn
ctTransIbmLlcLnmMode=_CtTransIbmLlcLnmMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,6),_CtTransIbmLlcLnmMode_Type())
ctTransIbmLlcLnmMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcLnmMode.setStatus(_A)
class _CtTransIbmLlcDscMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcDscMode_Type.__name__=_C
_CtTransIbmLlcDscMode_Object=MibTableColumn
ctTransIbmLlcDscMode=_CtTransIbmLlcDscMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,7),_CtTransIbmLlcDscMode_Type())
ctTransIbmLlcDscMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcDscMode.setStatus(_A)
class _CtTransIbmLlcOtherMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransIbmLlcOtherMode_Type.__name__=_C
_CtTransIbmLlcOtherMode_Object=MibTableColumn
ctTransIbmLlcOtherMode=_CtTransIbmLlcOtherMode_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,8),_CtTransIbmLlcOtherMode_Type())
ctTransIbmLlcOtherMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcOtherMode.setStatus(_A)
class _CtTransIbmLlcOtherValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtTransIbmLlcOtherValue_Type.__name__=_C
_CtTransIbmLlcOtherValue_Object=MibTableColumn
ctTransIbmLlcOtherValue=_CtTransIbmLlcOtherValue_Object((1,3,6,1,4,1,52,4,1,3,4,6,1,1,9),_CtTransIbmLlcOtherValue_Type())
ctTransIbmLlcOtherValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIbmLlcOtherValue.setStatus(_A)
_CtTransSr_ObjectIdentity=ObjectIdentity
ctTransSr=_CtTransSr_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,7))
_CtTransSrTable_Object=MibTable
ctTransSrTable=_CtTransSrTable_Object((1,3,6,1,4,1,52,4,1,3,4,7,1))
if mibBuilder.loadTexts:ctTransSrTable.setStatus(_A)
_CtTransSrEntry_Object=MibTableRow
ctTransSrEntry=_CtTransSrEntry_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1))
ctTransSrEntry.setIndexNames((0,_H,_W))
if mibBuilder.loadTexts:ctTransSrEntry.setStatus(_A)
_CtTransSrPort_Type=Integer32
_CtTransSrPort_Object=MibTableColumn
ctTransSrPort=_CtTransSrPort_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,1),_CtTransSrPort_Type())
ctTransSrPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransSrPort.setStatus(_A)
class _CtTransSrIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('srt',3)))
_CtTransSrIfMode_Type.__name__=_C
_CtTransSrIfMode_Object=MibTableColumn
ctTransSrIfMode=_CtTransSrIfMode_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,2),_CtTransSrIfMode_Type())
ctTransSrIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrIfMode.setStatus(_A)
class _CtTransSrExpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('are',2),('ste',3),('inboundtype',4)))
_CtTransSrExpMode_Type.__name__=_C
_CtTransSrExpMode_Object=MibTableColumn
ctTransSrExpMode=_CtTransSrExpMode_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,3),_CtTransSrExpMode_Type())
ctTransSrExpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrExpMode.setStatus(_A)
class _CtTransSrIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_F,4)))
_CtTransSrIP_Type.__name__=_C
_CtTransSrIP_Object=MibTableColumn
ctTransSrIP=_CtTransSrIP_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,4),_CtTransSrIP_Type())
ctTransSrIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrIP.setStatus(_A)
class _CtTransSrIPX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_F,4)))
_CtTransSrIPX_Type.__name__=_C
_CtTransSrIPX_Object=MibTableColumn
ctTransSrIPX=_CtTransSrIPX_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,5),_CtTransSrIPX_Type())
ctTransSrIPX.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrIPX.setStatus(_A)
class _CtTransSrNetBIOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_F,4)))
_CtTransSrNetBIOS_Type.__name__=_C
_CtTransSrNetBIOS_Object=MibTableColumn
ctTransSrNetBIOS=_CtTransSrNetBIOS_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,6),_CtTransSrNetBIOS_Type())
ctTransSrNetBIOS.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrNetBIOS.setStatus(_A)
class _CtTransSrSNA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_F,4)))
_CtTransSrSNA_Type.__name__=_C
_CtTransSrSNA_Object=MibTableColumn
ctTransSrSNA=_CtTransSrSNA_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,7),_CtTransSrSNA_Type())
ctTransSrSNA.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrSNA.setStatus(_A)
class _CtTransSrOther_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_CtTransSrOther_Type.__name__=_C
_CtTransSrOther_Object=MibTableColumn
ctTransSrOther=_CtTransSrOther_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,8),_CtTransSrOther_Type())
ctTransSrOther.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrOther.setStatus(_A)
_CtTransSRLocalSegment_Type=Integer32
_CtTransSRLocalSegment_Object=MibTableColumn
ctTransSRLocalSegment=_CtTransSRLocalSegment_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,9),_CtTransSRLocalSegment_Type())
ctTransSRLocalSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSRLocalSegment.setStatus(_A)
_CtTransSrSRLF_Type=Integer32
_CtTransSrSRLF_Object=MibTableColumn
ctTransSrSRLF=_CtTransSrSRLF_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,10),_CtTransSrSRLF_Type())
ctTransSrSRLF.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSrSRLF.setStatus(_A)
class _CtTransSRAutoRingNumberDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3)))
_CtTransSRAutoRingNumberDetect_Type.__name__=_C
_CtTransSRAutoRingNumberDetect_Object=MibTableColumn
ctTransSRAutoRingNumberDetect=_CtTransSRAutoRingNumberDetect_Object((1,3,6,1,4,1,52,4,1,3,4,7,1,1,11),_CtTransSRAutoRingNumberDetect_Type())
ctTransSRAutoRingNumberDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransSRAutoRingNumberDetect.setStatus(_A)
_CtTransNovellCfg_ObjectIdentity=ObjectIdentity
ctTransNovellCfg=_CtTransNovellCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,8))
_CtTransNovellCfgTable_Object=MibTable
ctTransNovellCfgTable=_CtTransNovellCfgTable_Object((1,3,6,1,4,1,52,4,1,3,4,8,1))
if mibBuilder.loadTexts:ctTransNovellCfgTable.setStatus(_A)
_CtTransNovellCfgEntry_Object=MibTableRow
ctTransNovellCfgEntry=_CtTransNovellCfgEntry_Object((1,3,6,1,4,1,52,4,1,3,4,8,1,1))
ctTransNovellCfgEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:ctTransNovellCfgEntry.setStatus(_A)
_CtTransNovellCfgPort_Type=Integer32
_CtTransNovellCfgPort_Object=MibTableColumn
ctTransNovellCfgPort=_CtTransNovellCfgPort_Object((1,3,6,1,4,1,52,4,1,3,4,8,1,1,1),_CtTransNovellCfgPort_Type())
ctTransNovellCfgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransNovellCfgPort.setStatus(_A)
class _CtTransNovellCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('enabledType2',3)))
_CtTransNovellCfgMode_Type.__name__=_C
_CtTransNovellCfgMode_Object=MibTableColumn
ctTransNovellCfgMode=_CtTransNovellCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,8,1,1,2),_CtTransNovellCfgMode_Type())
ctTransNovellCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransNovellCfgMode.setStatus(_A)
class _CtTransNovellGroupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtTransNovellGroupMode_Type.__name__=_C
_CtTransNovellGroupMode_Object=MibTableColumn
ctTransNovellGroupMode=_CtTransNovellGroupMode_Object((1,3,6,1,4,1,52,4,1,3,4,8,1,1,3),_CtTransNovellGroupMode_Type())
ctTransNovellGroupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransNovellGroupMode.setStatus(_A)
_CtTransIPCfg_ObjectIdentity=ObjectIdentity
ctTransIPCfg=_CtTransIPCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,9))
_CtTransIPCfgTable_Object=MibTable
ctTransIPCfgTable=_CtTransIPCfgTable_Object((1,3,6,1,4,1,52,4,1,3,4,9,1))
if mibBuilder.loadTexts:ctTransIPCfgTable.setStatus(_A)
_CtTransIPCfgEntry_Object=MibTableRow
ctTransIPCfgEntry=_CtTransIPCfgEntry_Object((1,3,6,1,4,1,52,4,1,3,4,9,1,1))
ctTransIPCfgEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:ctTransIPCfgEntry.setStatus(_A)
_CtTransIPCfgPort_Type=Integer32
_CtTransIPCfgPort_Object=MibTableColumn
ctTransIPCfgPort=_CtTransIPCfgPort_Object((1,3,6,1,4,1,52,4,1,3,4,9,1,1,1),_CtTransIPCfgPort_Type())
ctTransIPCfgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransIPCfgPort.setStatus(_A)
class _CtTransIPDataCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransIPDataCfgMode_Type.__name__=_C
_CtTransIPDataCfgMode_Object=MibTableColumn
ctTransIPDataCfgMode=_CtTransIPDataCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,9,1,1,2),_CtTransIPDataCfgMode_Type())
ctTransIPDataCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIPDataCfgMode.setStatus(_A)
class _CtTransIPArpCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransIPArpCfgMode_Type.__name__=_C
_CtTransIPArpCfgMode_Object=MibTableColumn
ctTransIPArpCfgMode=_CtTransIPArpCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,9,1,1,3),_CtTransIPArpCfgMode_Type())
ctTransIPArpCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIPArpCfgMode.setStatus(_A)
class _CtTransIPRarpCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransIPRarpCfgMode_Type.__name__=_C
_CtTransIPRarpCfgMode_Object=MibTableColumn
ctTransIPRarpCfgMode=_CtTransIPRarpCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,9,1,1,4),_CtTransIPRarpCfgMode_Type())
ctTransIPRarpCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransIPRarpCfgMode.setStatus(_A)
_CtTransA2Cfg_ObjectIdentity=ObjectIdentity
ctTransA2Cfg=_CtTransA2Cfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,10))
_CtTransA2CfgTable_Object=MibTable
ctTransA2CfgTable=_CtTransA2CfgTable_Object((1,3,6,1,4,1,52,4,1,3,4,10,1))
if mibBuilder.loadTexts:ctTransA2CfgTable.setStatus(_A)
_CtTransA2CfgEntry_Object=MibTableRow
ctTransA2CfgEntry=_CtTransA2CfgEntry_Object((1,3,6,1,4,1,52,4,1,3,4,10,1,1))
ctTransA2CfgEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:ctTransA2CfgEntry.setStatus(_A)
_CtTransA2CfgPort_Type=Integer32
_CtTransA2CfgPort_Object=MibTableColumn
ctTransA2CfgPort=_CtTransA2CfgPort_Object((1,3,6,1,4,1,52,4,1,3,4,10,1,1,1),_CtTransA2CfgPort_Type())
ctTransA2CfgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransA2CfgPort.setStatus(_A)
class _CtTransA2DataCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransA2DataCfgMode_Type.__name__=_C
_CtTransA2DataCfgMode_Object=MibTableColumn
ctTransA2DataCfgMode=_CtTransA2DataCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,10,1,1,2),_CtTransA2DataCfgMode_Type())
ctTransA2DataCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransA2DataCfgMode.setStatus(_A)
class _CtTransA2ArpCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransA2ArpCfgMode_Type.__name__=_C
_CtTransA2ArpCfgMode_Object=MibTableColumn
ctTransA2ArpCfgMode=_CtTransA2ArpCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,10,1,1,3),_CtTransA2ArpCfgMode_Type())
ctTransA2ArpCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransA2ArpCfgMode.setStatus(_A)
class _CtTransA2McastCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransA2McastCfgMode_Type.__name__=_C
_CtTransA2McastCfgMode_Object=MibTableColumn
ctTransA2McastCfgMode=_CtTransA2McastCfgMode_Object((1,3,6,1,4,1,52,4,1,3,4,10,1,1,4),_CtTransA2McastCfgMode_Type())
ctTransA2McastCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransA2McastCfgMode.setStatus(_A)
_CtTransOtherCfg_ObjectIdentity=ObjectIdentity
ctTransOtherCfg=_CtTransOtherCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,11))
_CtTransOtherTable_Object=MibTable
ctTransOtherTable=_CtTransOtherTable_Object((1,3,6,1,4,1,52,4,1,3,4,11,1))
if mibBuilder.loadTexts:ctTransOtherTable.setStatus(_A)
_CtTransOtherEntry_Object=MibTableRow
ctTransOtherEntry=_CtTransOtherEntry_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1))
ctTransOtherEntry.setIndexNames((0,_H,_a))
if mibBuilder.loadTexts:ctTransOtherEntry.setStatus(_A)
_CtTransOtherPort_Type=Integer32
_CtTransOtherPort_Object=MibTableColumn
ctTransOtherPort=_CtTransOtherPort_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,1),_CtTransOtherPort_Type())
ctTransOtherPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransOtherPort.setStatus(_A)
class _CtTransOtherUnknownSap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherUnknownSap_Type.__name__=_C
_CtTransOtherUnknownSap_Object=MibTableColumn
ctTransOtherUnknownSap=_CtTransOtherUnknownSap_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,2),_CtTransOtherUnknownSap_Type())
ctTransOtherUnknownSap.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherUnknownSap.setStatus(_A)
class _CtTransOtherUnknownSnap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherUnknownSnap_Type.__name__=_C
_CtTransOtherUnknownSnap_Object=MibTableColumn
ctTransOtherUnknownSnap=_CtTransOtherUnknownSnap_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,3),_CtTransOtherUnknownSnap_Type())
ctTransOtherUnknownSnap.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherUnknownSnap.setStatus(_A)
class _CtTransOtherSapDsap1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherSapDsap1Mode_Type.__name__=_C
_CtTransOtherSapDsap1Mode_Object=MibTableColumn
ctTransOtherSapDsap1Mode=_CtTransOtherSapDsap1Mode_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,4),_CtTransOtherSapDsap1Mode_Type())
ctTransOtherSapDsap1Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap1Mode.setStatus(_A)
class _CtTransOtherSapDsap1Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtTransOtherSapDsap1Val_Type.__name__=_C
_CtTransOtherSapDsap1Val_Object=MibTableColumn
ctTransOtherSapDsap1Val=_CtTransOtherSapDsap1Val_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,5),_CtTransOtherSapDsap1Val_Type())
ctTransOtherSapDsap1Val.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap1Val.setStatus(_A)
class _CtTransOtherSapDsap2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherSapDsap2Mode_Type.__name__=_C
_CtTransOtherSapDsap2Mode_Object=MibTableColumn
ctTransOtherSapDsap2Mode=_CtTransOtherSapDsap2Mode_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,6),_CtTransOtherSapDsap2Mode_Type())
ctTransOtherSapDsap2Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap2Mode.setStatus(_A)
class _CtTransOtherSapDsap2Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtTransOtherSapDsap2Val_Type.__name__=_C
_CtTransOtherSapDsap2Val_Object=MibTableColumn
ctTransOtherSapDsap2Val=_CtTransOtherSapDsap2Val_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,7),_CtTransOtherSapDsap2Val_Type())
ctTransOtherSapDsap2Val.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap2Val.setStatus(_A)
class _CtTransOtherSapDsap3Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherSapDsap3Mode_Type.__name__=_C
_CtTransOtherSapDsap3Mode_Object=MibTableColumn
ctTransOtherSapDsap3Mode=_CtTransOtherSapDsap3Mode_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,8),_CtTransOtherSapDsap3Mode_Type())
ctTransOtherSapDsap3Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap3Mode.setStatus(_A)
class _CtTransOtherSapDsap3Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CtTransOtherSapDsap3Val_Type.__name__=_C
_CtTransOtherSapDsap3Val_Object=MibTableColumn
ctTransOtherSapDsap3Val=_CtTransOtherSapDsap3Val_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,9),_CtTransOtherSapDsap3Val_Type())
ctTransOtherSapDsap3Val.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSapDsap3Val.setStatus(_A)
class _CtTransOtherSnap1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherSnap1Mode_Type.__name__=_C
_CtTransOtherSnap1Mode_Object=MibTableColumn
ctTransOtherSnap1Mode=_CtTransOtherSnap1Mode_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,10),_CtTransOtherSnap1Mode_Type())
ctTransOtherSnap1Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSnap1Mode.setStatus(_A)
class _CtTransOtherSnap1Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtTransOtherSnap1Val_Type.__name__=_C
_CtTransOtherSnap1Val_Object=MibTableColumn
ctTransOtherSnap1Val=_CtTransOtherSnap1Val_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,11),_CtTransOtherSnap1Val_Type())
ctTransOtherSnap1Val.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSnap1Val.setStatus(_A)
class _CtTransOtherSnap2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_CtTransOtherSnap2Mode_Type.__name__=_C
_CtTransOtherSnap2Mode_Object=MibTableColumn
ctTransOtherSnap2Mode=_CtTransOtherSnap2Mode_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,12),_CtTransOtherSnap2Mode_Type())
ctTransOtherSnap2Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSnap2Mode.setStatus(_A)
class _CtTransOtherSnap2Val_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtTransOtherSnap2Val_Type.__name__=_C
_CtTransOtherSnap2Val_Object=MibTableColumn
ctTransOtherSnap2Val=_CtTransOtherSnap2Val_Object((1,3,6,1,4,1,52,4,1,3,4,11,1,1,13),_CtTransOtherSnap2Val_Type())
ctTransOtherSnap2Val.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransOtherSnap2Val.setStatus(_A)
_CtTranslfpsCfg_ObjectIdentity=ObjectIdentity
ctTranslfpsCfg=_CtTranslfpsCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,3,4,12))
_CtTransLfpsTable_Object=MibTable
ctTransLfpsTable=_CtTransLfpsTable_Object((1,3,6,1,4,1,52,4,1,3,4,12,1))
if mibBuilder.loadTexts:ctTransLfpsTable.setStatus(_A)
_CtTransLfpsEntry_Object=MibTableRow
ctTransLfpsEntry=_CtTransLfpsEntry_Object((1,3,6,1,4,1,52,4,1,3,4,12,1,1))
ctTransLfpsEntry.setIndexNames((0,_H,_b))
if mibBuilder.loadTexts:ctTransLfpsEntry.setStatus(_A)
_CtTransLfpsPort_Type=Integer32
_CtTransLfpsPort_Object=MibTableColumn
ctTransLfpsPort=_CtTransLfpsPort_Object((1,3,6,1,4,1,52,4,1,3,4,12,1,1,1),_CtTransLfpsPort_Type())
ctTransLfpsPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransLfpsPort.setStatus(_A)
class _CtTransLfpsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('large',1),(_c,2),('small',3),(_K,4)))
_CtTransLfpsAdminStatus_Type.__name__=_C
_CtTransLfpsAdminStatus_Object=MibTableColumn
ctTransLfpsAdminStatus=_CtTransLfpsAdminStatus_Object((1,3,6,1,4,1,52,4,1,3,4,12,1,1,2),_CtTransLfpsAdminStatus_Type())
ctTransLfpsAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctTransLfpsAdminStatus.setStatus(_A)
class _CtTransLfpsOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('large',1),(_c,2),('small',3)))
_CtTransLfpsOperationalStatus_Type.__name__=_C
_CtTransLfpsOperationalStatus_Object=MibTableColumn
ctTransLfpsOperationalStatus=_CtTransLfpsOperationalStatus_Object((1,3,6,1,4,1,52,4,1,3,4,12,1,1,3),_CtTransLfpsOperationalStatus_Type())
ctTransLfpsOperationalStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ctTransLfpsOperationalStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ctTransFddiAtm':ctTransFddiAtm,'ctTransFddiAtmMtu':ctTransFddiAtmMtu,'ctTransFddiAtmIPFrag':ctTransFddiAtmIPFrag,'ctTransFddiEthernet':ctTransFddiEthernet,'ctTransFddiEthernetIPFrag':ctTransFddiEthernetIPFrag,'ctTransFddiSnapEthernetType':ctTransFddiSnapEthernetType,'ctTransFddiEthernetAuto':ctTransFddiEthernetAuto,'ctTransFddiEthernetSnapIPX':ctTransFddiEthernetSnapIPX,'ctTransFddiEthernet802dot2IPX':ctTransFddiEthernet802dot2IPX,'ctTransFddiEthernetMACIPX':ctTransFddiEthernetMACIPX,'ctTransEthernetFddi':ctTransEthernetFddi,'ctTransEthernetFddiRAW':ctTransEthernetFddiRAW,'ctTransEthernetFddiPadVerify':ctTransEthernetFddiPadVerify,'ctTransRifDb':ctTransRifDb,'ctTransRifDbTable':ctTransRifDbTable,'ctTransRifDbEntry':ctTransRifDbEntry,_S:ctTransRifDbMacAddr,'ctTransRifDbSrcPort':ctTransRifDbSrcPort,'ctTransRifDbLength':ctTransRifDbLength,'ctTransRifDbRIF':ctTransRifDbRIF,'ctTransRifDbCtrlTable':ctTransRifDbCtrlTable,'ctTransRifDbCtrlEntry':ctTransRifDbCtrlEntry,_T:ctTransRifDbCtrlPort,'ctTransRifDbWeightState':ctTransRifDbWeightState,'ctTransRifDbCtrlType':ctTransRifDbCtrlType,'ctTransRifDbAgingTimer':ctTransRifDbAgingTimer,'ctTransBcastX':ctTransBcastX,'ctTransBcastXTable':ctTransBcastXTable,'ctTransBcastXEntry':ctTransBcastXEntry,_U:ctTransBcastXPort,'ctTransBcastXMode':ctTransBcastXMode,'ctTransBcastXMedia':ctTransBcastXMedia,'ctTransBcastXCanonical':ctTransBcastXCanonical,'ctTransIbmLlc':ctTransIbmLlc,'ctTransIbmLlcTable':ctTransIbmLlcTable,'ctTransIbmLlcEntry':ctTransIbmLlcEntry,_V:ctTransIbmLlcPort,'ctTransIbmLlcNullMode':ctTransIbmLlcNullMode,'ctTransIbmLlcSnaPathMode':ctTransIbmLlcSnaPathMode,'ctTransIbmLlcSnaMode':ctTransIbmLlcSnaMode,'ctTransIbmLlcNbMode':ctTransIbmLlcNbMode,'ctTransIbmLlcLnmMode':ctTransIbmLlcLnmMode,'ctTransIbmLlcDscMode':ctTransIbmLlcDscMode,'ctTransIbmLlcOtherMode':ctTransIbmLlcOtherMode,'ctTransIbmLlcOtherValue':ctTransIbmLlcOtherValue,'ctTransSr':ctTransSr,'ctTransSrTable':ctTransSrTable,'ctTransSrEntry':ctTransSrEntry,_W:ctTransSrPort,'ctTransSrIfMode':ctTransSrIfMode,'ctTransSrExpMode':ctTransSrExpMode,'ctTransSrIP':ctTransSrIP,'ctTransSrIPX':ctTransSrIPX,'ctTransSrNetBIOS':ctTransSrNetBIOS,'ctTransSrSNA':ctTransSrSNA,'ctTransSrOther':ctTransSrOther,'ctTransSRLocalSegment':ctTransSRLocalSegment,'ctTransSrSRLF':ctTransSrSRLF,'ctTransSRAutoRingNumberDetect':ctTransSRAutoRingNumberDetect,'ctTransNovellCfg':ctTransNovellCfg,'ctTransNovellCfgTable':ctTransNovellCfgTable,'ctTransNovellCfgEntry':ctTransNovellCfgEntry,_X:ctTransNovellCfgPort,'ctTransNovellCfgMode':ctTransNovellCfgMode,'ctTransNovellGroupMode':ctTransNovellGroupMode,'ctTransIPCfg':ctTransIPCfg,'ctTransIPCfgTable':ctTransIPCfgTable,'ctTransIPCfgEntry':ctTransIPCfgEntry,_Y:ctTransIPCfgPort,'ctTransIPDataCfgMode':ctTransIPDataCfgMode,'ctTransIPArpCfgMode':ctTransIPArpCfgMode,'ctTransIPRarpCfgMode':ctTransIPRarpCfgMode,'ctTransA2Cfg':ctTransA2Cfg,'ctTransA2CfgTable':ctTransA2CfgTable,'ctTransA2CfgEntry':ctTransA2CfgEntry,_Z:ctTransA2CfgPort,'ctTransA2DataCfgMode':ctTransA2DataCfgMode,'ctTransA2ArpCfgMode':ctTransA2ArpCfgMode,'ctTransA2McastCfgMode':ctTransA2McastCfgMode,'ctTransOtherCfg':ctTransOtherCfg,'ctTransOtherTable':ctTransOtherTable,'ctTransOtherEntry':ctTransOtherEntry,_a:ctTransOtherPort,'ctTransOtherUnknownSap':ctTransOtherUnknownSap,'ctTransOtherUnknownSnap':ctTransOtherUnknownSnap,'ctTransOtherSapDsap1Mode':ctTransOtherSapDsap1Mode,'ctTransOtherSapDsap1Val':ctTransOtherSapDsap1Val,'ctTransOtherSapDsap2Mode':ctTransOtherSapDsap2Mode,'ctTransOtherSapDsap2Val':ctTransOtherSapDsap2Val,'ctTransOtherSapDsap3Mode':ctTransOtherSapDsap3Mode,'ctTransOtherSapDsap3Val':ctTransOtherSapDsap3Val,'ctTransOtherSnap1Mode':ctTransOtherSnap1Mode,'ctTransOtherSnap1Val':ctTransOtherSnap1Val,'ctTransOtherSnap2Mode':ctTransOtherSnap2Mode,'ctTransOtherSnap2Val':ctTransOtherSnap2Val,'ctTranslfpsCfg':ctTranslfpsCfg,'ctTransLfpsTable':ctTransLfpsTable,'ctTransLfpsEntry':ctTransLfpsEntry,_b:ctTransLfpsPort,'ctTransLfpsAdminStatus':ctTransLfpsAdminStatus,'ctTransLfpsOperationalStatus':ctTransLfpsOperationalStatus})