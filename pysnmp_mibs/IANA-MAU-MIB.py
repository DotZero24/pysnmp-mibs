_W='b100GbaseKP4'
_V='b100GbaseKR4'
_U='b100GbaseCR4'
_T='b40GbaseT'
_S='b25GbaseT'
_R='b25GbaseR'
_Q='b1000baseT1'
_P='b100GbaseCR10'
_O='b40GbaseCR4'
_N='b40GbaseKR4'
_M='b10GbaseKR'
_L='b10GbaseKX4'
_K='b1000baseKX'
_J='b10GbaseT'
_I='b1000baseTFD'
_H='b1000baseXFD'
_G='b100baseT2FD'
_F='b100baseTXFD'
_E='b100baseT4'
_D='b10baseTFD'
_C='b10baseT'
_B='bOther'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ianaMauMIB=ModuleIdentity((1,3,6,1,2,1,154))
if mibBuilder.loadTexts:ianaMauMIB.setRevisions(('2017-04-10 00:00','2014-08-01 00:00','2014-05-22 00:00','2011-08-12 00:00','2010-02-23 00:00','2007-04-21 00:00'))
class IANAifMauTypeListBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_B,0),('bAUI',1),('b10base5',2),('bFoirl',3),('b10base2',4),(_C,5),('b10baseFP',6),('b10baseFB',7),('b10baseFL',8),('b10broad36',9),('b10baseTHD',10),(_D,11),('b10baseFLHD',12),('b10baseFLFD',13),(_E,14),('b100baseTXHD',15),(_F,16),('b100baseFXHD',17),('b100baseFXFD',18),('b100baseT2HD',19),(_G,20),('b1000baseXHD',21),(_H,22),('b1000baseLXHD',23),('b1000baseLXFD',24),('b1000baseSXHD',25),('b1000baseSXFD',26),('b1000baseCXHD',27),('b1000baseCXFD',28),('b1000baseTHD',29),(_I,30),('b10GbaseX',31),('b10GbaseLX4',32),('b10GbaseR',33),('b10GbaseER',34),('b10GbaseLR',35),('b10GbaseSR',36),('b10GbaseW',37),('b10GbaseEW',38),('b10GbaseLW',39),('b10GbaseSW',40),('b10GbaseCX4',41),('b2BaseTL',42),('b10PassTS',43),('b100BaseBX10D',44),('b100BaseBX10U',45),('b100BaseLX10',46),('b1000BaseBX10D',47),('b1000BaseBX10U',48),('b1000BaseLX10',49),('b1000BasePX10D',50),('b1000BasePX10U',51),('b1000BasePX20D',52),('b1000BasePX20U',53),(_J,54),('b10GbaseLRM',55),(_K,56),(_L,57),(_M,58),('b10G1GbasePRXD1',59),('b10G1GbasePRXD2',60),('b10G1GbasePRXD3',61),('b10G1GbasePRXU1',62),('b10G1GbasePRXU2',63),('b10G1GbasePRXU3',64),('b10GbasePRD1',65),('b10GbasePRD2',66),('b10GbasePRD3',67),('b10GbasePRU1',68),('b10GbasePRU3',69),(_N,70),(_O,71),('b40GbaseSR4',72),('b40GbaseFR',73),('b40GbaseLR4',74),(_P,75),('b100GbaseSR10',76),('b100GbaseLR4',77),('b100GbaseER4',78),(_Q,79),('b1000basePX30D',80),('b1000basePX30U',81),('b1000basePX40D',82),('b1000basePX40U',83),('b10G1GbasePRXD4',84),('b10G1GbasePRXU4',85),('b10GbasePRD4',86),('b10GbasePRU4',87),('b25GbaseCR',88),('b25GbaseCRS',89),('b25GbaseKR',90),('b25GbaseKRS',91),(_R,92),('b25GbaseSR',93),(_S,94),('b40GbaseER4',95),('b40GbaseR',96),(_T,97),(_U,98),(_V,99),(_W,100),('b100GbaseR',101),('b100GbaseSR4',102),('b2p5GbaseT',103),('b5GbaseT',104)))
class IANAifMauMediaAvailable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('other',1),('unknown',2),('available',3),('notAvailable',4),('remoteFault',5),('invalidSignal',6),('remoteJabber',7),('remoteLinkLoss',8),('remoteTest',9),('offline',10),('autoNegError',11),('pmdLinkFault',12),('wisFrameLoss',13),('wisSignalLoss',14),('pcsLinkFault',15),('excessiveBER',16),('dxsLinkFault',17),('pxsLinkFault',18),('availableReduced',19),('ready',20)))
class IANAifMauAutoNegCapBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_B,0),(_C,1),(_D,2),(_E,3),('b100baseTX',4),(_F,5),('b100baseT2',6),(_G,7),('bFdxPause',8),('bFdxAPause',9),('bFdxSPause',10),('bFdxBPause',11),('b1000baseX',12),(_H,13),('b1000baseT',14),(_I,15),(_J,16),(_K,17),(_L,18),(_M,19),(_N,20),(_O,21),(_P,22),(_Q,23),('b25GbaseRS',24),(_R,25),('bRSFEC25Greq',26),('bBaseFEC25Greq',27),(_S,28),(_T,29),(_U,30),(_V,31),(_W,32),('bForceMS',33)))
class IANAifJackType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('rj45',2),('rj45S',3),('db9',4),('bnc',5),('fAUI',6),('mAUI',7),('fiberSC',8),('fiberMIC',9),('fiberST',10),('telco',11),('mtrj',12),('hssdc',13),('fiberLC',14),('cx4',15),('sfpPlusDA',16)))
_Dot3MauType_ObjectIdentity=ObjectIdentity
dot3MauType=_Dot3MauType_ObjectIdentity((1,3,6,1,2,1,26,4))
_Dot3MauTypeAUI_ObjectIdentity=ObjectIdentity
dot3MauTypeAUI=_Dot3MauTypeAUI_ObjectIdentity((1,3,6,1,2,1,26,4,1))
if mibBuilder.loadTexts:dot3MauTypeAUI.setStatus(_A)
_Dot3MauType10Base5_ObjectIdentity=ObjectIdentity
dot3MauType10Base5=_Dot3MauType10Base5_ObjectIdentity((1,3,6,1,2,1,26,4,2))
if mibBuilder.loadTexts:dot3MauType10Base5.setStatus(_A)
_Dot3MauTypeFoirl_ObjectIdentity=ObjectIdentity
dot3MauTypeFoirl=_Dot3MauTypeFoirl_ObjectIdentity((1,3,6,1,2,1,26,4,3))
if mibBuilder.loadTexts:dot3MauTypeFoirl.setStatus(_A)
_Dot3MauType10Base2_ObjectIdentity=ObjectIdentity
dot3MauType10Base2=_Dot3MauType10Base2_ObjectIdentity((1,3,6,1,2,1,26,4,4))
if mibBuilder.loadTexts:dot3MauType10Base2.setStatus(_A)
_Dot3MauType10BaseT_ObjectIdentity=ObjectIdentity
dot3MauType10BaseT=_Dot3MauType10BaseT_ObjectIdentity((1,3,6,1,2,1,26,4,5))
if mibBuilder.loadTexts:dot3MauType10BaseT.setStatus(_A)
_Dot3MauType10BaseFP_ObjectIdentity=ObjectIdentity
dot3MauType10BaseFP=_Dot3MauType10BaseFP_ObjectIdentity((1,3,6,1,2,1,26,4,6))
if mibBuilder.loadTexts:dot3MauType10BaseFP.setStatus(_A)
_Dot3MauType10BaseFB_ObjectIdentity=ObjectIdentity
dot3MauType10BaseFB=_Dot3MauType10BaseFB_ObjectIdentity((1,3,6,1,2,1,26,4,7))
if mibBuilder.loadTexts:dot3MauType10BaseFB.setStatus(_A)
_Dot3MauType10BaseFL_ObjectIdentity=ObjectIdentity
dot3MauType10BaseFL=_Dot3MauType10BaseFL_ObjectIdentity((1,3,6,1,2,1,26,4,8))
if mibBuilder.loadTexts:dot3MauType10BaseFL.setStatus(_A)
_Dot3MauType10Broad36_ObjectIdentity=ObjectIdentity
dot3MauType10Broad36=_Dot3MauType10Broad36_ObjectIdentity((1,3,6,1,2,1,26,4,9))
if mibBuilder.loadTexts:dot3MauType10Broad36.setStatus(_A)
_Dot3MauType10BaseTHD_ObjectIdentity=ObjectIdentity
dot3MauType10BaseTHD=_Dot3MauType10BaseTHD_ObjectIdentity((1,3,6,1,2,1,26,4,10))
if mibBuilder.loadTexts:dot3MauType10BaseTHD.setStatus(_A)
_Dot3MauType10BaseTFD_ObjectIdentity=ObjectIdentity
dot3MauType10BaseTFD=_Dot3MauType10BaseTFD_ObjectIdentity((1,3,6,1,2,1,26,4,11))
if mibBuilder.loadTexts:dot3MauType10BaseTFD.setStatus(_A)
_Dot3MauType10BaseFLHD_ObjectIdentity=ObjectIdentity
dot3MauType10BaseFLHD=_Dot3MauType10BaseFLHD_ObjectIdentity((1,3,6,1,2,1,26,4,12))
if mibBuilder.loadTexts:dot3MauType10BaseFLHD.setStatus(_A)
_Dot3MauType10BaseFLFD_ObjectIdentity=ObjectIdentity
dot3MauType10BaseFLFD=_Dot3MauType10BaseFLFD_ObjectIdentity((1,3,6,1,2,1,26,4,13))
if mibBuilder.loadTexts:dot3MauType10BaseFLFD.setStatus(_A)
_Dot3MauType100BaseT4_ObjectIdentity=ObjectIdentity
dot3MauType100BaseT4=_Dot3MauType100BaseT4_ObjectIdentity((1,3,6,1,2,1,26,4,14))
if mibBuilder.loadTexts:dot3MauType100BaseT4.setStatus(_A)
_Dot3MauType100BaseTXHD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseTXHD=_Dot3MauType100BaseTXHD_ObjectIdentity((1,3,6,1,2,1,26,4,15))
if mibBuilder.loadTexts:dot3MauType100BaseTXHD.setStatus(_A)
_Dot3MauType100BaseTXFD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseTXFD=_Dot3MauType100BaseTXFD_ObjectIdentity((1,3,6,1,2,1,26,4,16))
if mibBuilder.loadTexts:dot3MauType100BaseTXFD.setStatus(_A)
_Dot3MauType100BaseFXHD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseFXHD=_Dot3MauType100BaseFXHD_ObjectIdentity((1,3,6,1,2,1,26,4,17))
if mibBuilder.loadTexts:dot3MauType100BaseFXHD.setStatus(_A)
_Dot3MauType100BaseFXFD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseFXFD=_Dot3MauType100BaseFXFD_ObjectIdentity((1,3,6,1,2,1,26,4,18))
if mibBuilder.loadTexts:dot3MauType100BaseFXFD.setStatus(_A)
_Dot3MauType100BaseT2HD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseT2HD=_Dot3MauType100BaseT2HD_ObjectIdentity((1,3,6,1,2,1,26,4,19))
if mibBuilder.loadTexts:dot3MauType100BaseT2HD.setStatus(_A)
_Dot3MauType100BaseT2FD_ObjectIdentity=ObjectIdentity
dot3MauType100BaseT2FD=_Dot3MauType100BaseT2FD_ObjectIdentity((1,3,6,1,2,1,26,4,20))
if mibBuilder.loadTexts:dot3MauType100BaseT2FD.setStatus(_A)
_Dot3MauType1000BaseXHD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseXHD=_Dot3MauType1000BaseXHD_ObjectIdentity((1,3,6,1,2,1,26,4,21))
if mibBuilder.loadTexts:dot3MauType1000BaseXHD.setStatus(_A)
_Dot3MauType1000BaseXFD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseXFD=_Dot3MauType1000BaseXFD_ObjectIdentity((1,3,6,1,2,1,26,4,22))
if mibBuilder.loadTexts:dot3MauType1000BaseXFD.setStatus(_A)
_Dot3MauType1000BaseLXHD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseLXHD=_Dot3MauType1000BaseLXHD_ObjectIdentity((1,3,6,1,2,1,26,4,23))
if mibBuilder.loadTexts:dot3MauType1000BaseLXHD.setStatus(_A)
_Dot3MauType1000BaseLXFD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseLXFD=_Dot3MauType1000BaseLXFD_ObjectIdentity((1,3,6,1,2,1,26,4,24))
if mibBuilder.loadTexts:dot3MauType1000BaseLXFD.setStatus(_A)
_Dot3MauType1000BaseSXHD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseSXHD=_Dot3MauType1000BaseSXHD_ObjectIdentity((1,3,6,1,2,1,26,4,25))
if mibBuilder.loadTexts:dot3MauType1000BaseSXHD.setStatus(_A)
_Dot3MauType1000BaseSXFD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseSXFD=_Dot3MauType1000BaseSXFD_ObjectIdentity((1,3,6,1,2,1,26,4,26))
if mibBuilder.loadTexts:dot3MauType1000BaseSXFD.setStatus(_A)
_Dot3MauType1000BaseCXHD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseCXHD=_Dot3MauType1000BaseCXHD_ObjectIdentity((1,3,6,1,2,1,26,4,27))
if mibBuilder.loadTexts:dot3MauType1000BaseCXHD.setStatus(_A)
_Dot3MauType1000BaseCXFD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseCXFD=_Dot3MauType1000BaseCXFD_ObjectIdentity((1,3,6,1,2,1,26,4,28))
if mibBuilder.loadTexts:dot3MauType1000BaseCXFD.setStatus(_A)
_Dot3MauType1000BaseTHD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseTHD=_Dot3MauType1000BaseTHD_ObjectIdentity((1,3,6,1,2,1,26,4,29))
if mibBuilder.loadTexts:dot3MauType1000BaseTHD.setStatus(_A)
_Dot3MauType1000BaseTFD_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseTFD=_Dot3MauType1000BaseTFD_ObjectIdentity((1,3,6,1,2,1,26,4,30))
if mibBuilder.loadTexts:dot3MauType1000BaseTFD.setStatus(_A)
_Dot3MauType10GigBaseX_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseX=_Dot3MauType10GigBaseX_ObjectIdentity((1,3,6,1,2,1,26,4,31))
if mibBuilder.loadTexts:dot3MauType10GigBaseX.setStatus(_A)
_Dot3MauType10GigBaseLX4_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseLX4=_Dot3MauType10GigBaseLX4_ObjectIdentity((1,3,6,1,2,1,26,4,32))
if mibBuilder.loadTexts:dot3MauType10GigBaseLX4.setStatus(_A)
_Dot3MauType10GigBaseR_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseR=_Dot3MauType10GigBaseR_ObjectIdentity((1,3,6,1,2,1,26,4,33))
if mibBuilder.loadTexts:dot3MauType10GigBaseR.setStatus(_A)
_Dot3MauType10GigBaseER_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseER=_Dot3MauType10GigBaseER_ObjectIdentity((1,3,6,1,2,1,26,4,34))
if mibBuilder.loadTexts:dot3MauType10GigBaseER.setStatus(_A)
_Dot3MauType10GigBaseLR_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseLR=_Dot3MauType10GigBaseLR_ObjectIdentity((1,3,6,1,2,1,26,4,35))
if mibBuilder.loadTexts:dot3MauType10GigBaseLR.setStatus(_A)
_Dot3MauType10GigBaseSR_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseSR=_Dot3MauType10GigBaseSR_ObjectIdentity((1,3,6,1,2,1,26,4,36))
if mibBuilder.loadTexts:dot3MauType10GigBaseSR.setStatus(_A)
_Dot3MauType10GigBaseW_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseW=_Dot3MauType10GigBaseW_ObjectIdentity((1,3,6,1,2,1,26,4,37))
if mibBuilder.loadTexts:dot3MauType10GigBaseW.setStatus(_A)
_Dot3MauType10GigBaseEW_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseEW=_Dot3MauType10GigBaseEW_ObjectIdentity((1,3,6,1,2,1,26,4,38))
if mibBuilder.loadTexts:dot3MauType10GigBaseEW.setStatus(_A)
_Dot3MauType10GigBaseLW_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseLW=_Dot3MauType10GigBaseLW_ObjectIdentity((1,3,6,1,2,1,26,4,39))
if mibBuilder.loadTexts:dot3MauType10GigBaseLW.setStatus(_A)
_Dot3MauType10GigBaseSW_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseSW=_Dot3MauType10GigBaseSW_ObjectIdentity((1,3,6,1,2,1,26,4,40))
if mibBuilder.loadTexts:dot3MauType10GigBaseSW.setStatus(_A)
_Dot3MauType10GigBaseCX4_ObjectIdentity=ObjectIdentity
dot3MauType10GigBaseCX4=_Dot3MauType10GigBaseCX4_ObjectIdentity((1,3,6,1,2,1,26,4,41))
if mibBuilder.loadTexts:dot3MauType10GigBaseCX4.setStatus(_A)
_Dot3MauType2BaseTL_ObjectIdentity=ObjectIdentity
dot3MauType2BaseTL=_Dot3MauType2BaseTL_ObjectIdentity((1,3,6,1,2,1,26,4,42))
if mibBuilder.loadTexts:dot3MauType2BaseTL.setStatus(_A)
_Dot3MauType10PassTS_ObjectIdentity=ObjectIdentity
dot3MauType10PassTS=_Dot3MauType10PassTS_ObjectIdentity((1,3,6,1,2,1,26,4,43))
if mibBuilder.loadTexts:dot3MauType10PassTS.setStatus(_A)
_Dot3MauType100BaseBX10D_ObjectIdentity=ObjectIdentity
dot3MauType100BaseBX10D=_Dot3MauType100BaseBX10D_ObjectIdentity((1,3,6,1,2,1,26,4,44))
if mibBuilder.loadTexts:dot3MauType100BaseBX10D.setStatus(_A)
_Dot3MauType100BaseBX10U_ObjectIdentity=ObjectIdentity
dot3MauType100BaseBX10U=_Dot3MauType100BaseBX10U_ObjectIdentity((1,3,6,1,2,1,26,4,45))
if mibBuilder.loadTexts:dot3MauType100BaseBX10U.setStatus(_A)
_Dot3MauType100BaseLX10_ObjectIdentity=ObjectIdentity
dot3MauType100BaseLX10=_Dot3MauType100BaseLX10_ObjectIdentity((1,3,6,1,2,1,26,4,46))
if mibBuilder.loadTexts:dot3MauType100BaseLX10.setStatus(_A)
_Dot3MauType1000BaseBX10D_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseBX10D=_Dot3MauType1000BaseBX10D_ObjectIdentity((1,3,6,1,2,1,26,4,47))
if mibBuilder.loadTexts:dot3MauType1000BaseBX10D.setStatus(_A)
_Dot3MauType1000BaseBX10U_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseBX10U=_Dot3MauType1000BaseBX10U_ObjectIdentity((1,3,6,1,2,1,26,4,48))
if mibBuilder.loadTexts:dot3MauType1000BaseBX10U.setStatus(_A)
_Dot3MauType1000BaseLX10_ObjectIdentity=ObjectIdentity
dot3MauType1000BaseLX10=_Dot3MauType1000BaseLX10_ObjectIdentity((1,3,6,1,2,1,26,4,49))
if mibBuilder.loadTexts:dot3MauType1000BaseLX10.setStatus(_A)
_Dot3MauType1000BasePX10D_ObjectIdentity=ObjectIdentity
dot3MauType1000BasePX10D=_Dot3MauType1000BasePX10D_ObjectIdentity((1,3,6,1,2,1,26,4,50))
if mibBuilder.loadTexts:dot3MauType1000BasePX10D.setStatus(_A)
_Dot3MauType1000BasePX10U_ObjectIdentity=ObjectIdentity
dot3MauType1000BasePX10U=_Dot3MauType1000BasePX10U_ObjectIdentity((1,3,6,1,2,1,26,4,51))
if mibBuilder.loadTexts:dot3MauType1000BasePX10U.setStatus(_A)
_Dot3MauType1000BasePX20D_ObjectIdentity=ObjectIdentity
dot3MauType1000BasePX20D=_Dot3MauType1000BasePX20D_ObjectIdentity((1,3,6,1,2,1,26,4,52))
if mibBuilder.loadTexts:dot3MauType1000BasePX20D.setStatus(_A)
_Dot3MauType1000BasePX20U_ObjectIdentity=ObjectIdentity
dot3MauType1000BasePX20U=_Dot3MauType1000BasePX20U_ObjectIdentity((1,3,6,1,2,1,26,4,53))
if mibBuilder.loadTexts:dot3MauType1000BasePX20U.setStatus(_A)
_Dot3MauType10GbaseT_ObjectIdentity=ObjectIdentity
dot3MauType10GbaseT=_Dot3MauType10GbaseT_ObjectIdentity((1,3,6,1,2,1,26,4,54))
if mibBuilder.loadTexts:dot3MauType10GbaseT.setStatus(_A)
_Dot3MauType10GbaseLRM_ObjectIdentity=ObjectIdentity
dot3MauType10GbaseLRM=_Dot3MauType10GbaseLRM_ObjectIdentity((1,3,6,1,2,1,26,4,55))
if mibBuilder.loadTexts:dot3MauType10GbaseLRM.setStatus(_A)
_Dot3MauType1000baseKX_ObjectIdentity=ObjectIdentity
dot3MauType1000baseKX=_Dot3MauType1000baseKX_ObjectIdentity((1,3,6,1,2,1,26,4,56))
if mibBuilder.loadTexts:dot3MauType1000baseKX.setStatus(_A)
_Dot3MauType10GbaseKX4_ObjectIdentity=ObjectIdentity
dot3MauType10GbaseKX4=_Dot3MauType10GbaseKX4_ObjectIdentity((1,3,6,1,2,1,26,4,57))
if mibBuilder.loadTexts:dot3MauType10GbaseKX4.setStatus(_A)
_Dot3MauType10GbaseKR_ObjectIdentity=ObjectIdentity
dot3MauType10GbaseKR=_Dot3MauType10GbaseKR_ObjectIdentity((1,3,6,1,2,1,26,4,58))
if mibBuilder.loadTexts:dot3MauType10GbaseKR.setStatus(_A)
_Dot3MauType10G1GbasePRXD1_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXD1=_Dot3MauType10G1GbasePRXD1_ObjectIdentity((1,3,6,1,2,1,26,4,59))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXD1.setStatus(_A)
_Dot3MauType10G1GbasePRXD2_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXD2=_Dot3MauType10G1GbasePRXD2_ObjectIdentity((1,3,6,1,2,1,26,4,60))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXD2.setStatus(_A)
_Dot3MauType10G1GbasePRXD3_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXD3=_Dot3MauType10G1GbasePRXD3_ObjectIdentity((1,3,6,1,2,1,26,4,61))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXD3.setStatus(_A)
_Dot3MauType10G1GbasePRXU1_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXU1=_Dot3MauType10G1GbasePRXU1_ObjectIdentity((1,3,6,1,2,1,26,4,62))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXU1.setStatus(_A)
_Dot3MauType10G1GbasePRXU2_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXU2=_Dot3MauType10G1GbasePRXU2_ObjectIdentity((1,3,6,1,2,1,26,4,63))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXU2.setStatus(_A)
_Dot3MauType10G1GbasePRXU3_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXU3=_Dot3MauType10G1GbasePRXU3_ObjectIdentity((1,3,6,1,2,1,26,4,64))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXU3.setStatus(_A)
_Dot3MauType10GbasePRD1_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRD1=_Dot3MauType10GbasePRD1_ObjectIdentity((1,3,6,1,2,1,26,4,65))
if mibBuilder.loadTexts:dot3MauType10GbasePRD1.setStatus(_A)
_Dot3MauType10GbasePRD2_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRD2=_Dot3MauType10GbasePRD2_ObjectIdentity((1,3,6,1,2,1,26,4,66))
if mibBuilder.loadTexts:dot3MauType10GbasePRD2.setStatus(_A)
_Dot3MauType10GbasePRD3_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRD3=_Dot3MauType10GbasePRD3_ObjectIdentity((1,3,6,1,2,1,26,4,67))
if mibBuilder.loadTexts:dot3MauType10GbasePRD3.setStatus(_A)
_Dot3MauType10GbasePRU1_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRU1=_Dot3MauType10GbasePRU1_ObjectIdentity((1,3,6,1,2,1,26,4,68))
if mibBuilder.loadTexts:dot3MauType10GbasePRU1.setStatus(_A)
_Dot3MauType10GbasePRU3_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRU3=_Dot3MauType10GbasePRU3_ObjectIdentity((1,3,6,1,2,1,26,4,69))
if mibBuilder.loadTexts:dot3MauType10GbasePRU3.setStatus(_A)
_Dot3MauType40GbaseKR4_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseKR4=_Dot3MauType40GbaseKR4_ObjectIdentity((1,3,6,1,2,1,26,4,70))
if mibBuilder.loadTexts:dot3MauType40GbaseKR4.setStatus(_A)
_Dot3MauType40GbaseCR4_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseCR4=_Dot3MauType40GbaseCR4_ObjectIdentity((1,3,6,1,2,1,26,4,71))
if mibBuilder.loadTexts:dot3MauType40GbaseCR4.setStatus(_A)
_Dot3MauType40GbaseSR4_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseSR4=_Dot3MauType40GbaseSR4_ObjectIdentity((1,3,6,1,2,1,26,4,72))
if mibBuilder.loadTexts:dot3MauType40GbaseSR4.setStatus(_A)
_Dot3MauType40GbaseFR_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseFR=_Dot3MauType40GbaseFR_ObjectIdentity((1,3,6,1,2,1,26,4,73))
if mibBuilder.loadTexts:dot3MauType40GbaseFR.setStatus(_A)
_Dot3MauType40GbaseLR4_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseLR4=_Dot3MauType40GbaseLR4_ObjectIdentity((1,3,6,1,2,1,26,4,74))
if mibBuilder.loadTexts:dot3MauType40GbaseLR4.setStatus(_A)
_Dot3MauType100GbaseCR10_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseCR10=_Dot3MauType100GbaseCR10_ObjectIdentity((1,3,6,1,2,1,26,4,75))
if mibBuilder.loadTexts:dot3MauType100GbaseCR10.setStatus(_A)
_Dot3MauType100GbaseSR10_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseSR10=_Dot3MauType100GbaseSR10_ObjectIdentity((1,3,6,1,2,1,26,4,76))
if mibBuilder.loadTexts:dot3MauType100GbaseSR10.setStatus(_A)
_Dot3MauType100GbaseLR4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseLR4=_Dot3MauType100GbaseLR4_ObjectIdentity((1,3,6,1,2,1,26,4,77))
if mibBuilder.loadTexts:dot3MauType100GbaseLR4.setStatus(_A)
_Dot3MauType100GbaseER4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseER4=_Dot3MauType100GbaseER4_ObjectIdentity((1,3,6,1,2,1,26,4,78))
if mibBuilder.loadTexts:dot3MauType100GbaseER4.setStatus(_A)
_Dot3MauType1000baseT1_ObjectIdentity=ObjectIdentity
dot3MauType1000baseT1=_Dot3MauType1000baseT1_ObjectIdentity((1,3,6,1,2,1,26,4,79))
if mibBuilder.loadTexts:dot3MauType1000baseT1.setStatus(_A)
_Dot3MauType1000basePX30D_ObjectIdentity=ObjectIdentity
dot3MauType1000basePX30D=_Dot3MauType1000basePX30D_ObjectIdentity((1,3,6,1,2,1,26,4,80))
if mibBuilder.loadTexts:dot3MauType1000basePX30D.setStatus(_A)
_Dot3MauType1000basePX30U_ObjectIdentity=ObjectIdentity
dot3MauType1000basePX30U=_Dot3MauType1000basePX30U_ObjectIdentity((1,3,6,1,2,1,26,4,81))
if mibBuilder.loadTexts:dot3MauType1000basePX30U.setStatus(_A)
_Dot3MauType1000basePX40D_ObjectIdentity=ObjectIdentity
dot3MauType1000basePX40D=_Dot3MauType1000basePX40D_ObjectIdentity((1,3,6,1,2,1,26,4,82))
if mibBuilder.loadTexts:dot3MauType1000basePX40D.setStatus(_A)
_Dot3MauType1000basePX40U_ObjectIdentity=ObjectIdentity
dot3MauType1000basePX40U=_Dot3MauType1000basePX40U_ObjectIdentity((1,3,6,1,2,1,26,4,83))
if mibBuilder.loadTexts:dot3MauType1000basePX40U.setStatus(_A)
_Dot3MauType10G1GbasePRXD4_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXD4=_Dot3MauType10G1GbasePRXD4_ObjectIdentity((1,3,6,1,2,1,26,4,84))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXD4.setStatus(_A)
_Dot3MauType10G1GbasePRXU4_ObjectIdentity=ObjectIdentity
dot3MauType10G1GbasePRXU4=_Dot3MauType10G1GbasePRXU4_ObjectIdentity((1,3,6,1,2,1,26,4,85))
if mibBuilder.loadTexts:dot3MauType10G1GbasePRXU4.setStatus(_A)
_Dot3MauType10GbasePRD4_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRD4=_Dot3MauType10GbasePRD4_ObjectIdentity((1,3,6,1,2,1,26,4,86))
if mibBuilder.loadTexts:dot3MauType10GbasePRD4.setStatus(_A)
_Dot3MauType10GbasePRU4_ObjectIdentity=ObjectIdentity
dot3MauType10GbasePRU4=_Dot3MauType10GbasePRU4_ObjectIdentity((1,3,6,1,2,1,26,4,87))
if mibBuilder.loadTexts:dot3MauType10GbasePRU4.setStatus(_A)
_Dot3MauType25GbaseCR_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseCR=_Dot3MauType25GbaseCR_ObjectIdentity((1,3,6,1,2,1,26,4,88))
if mibBuilder.loadTexts:dot3MauType25GbaseCR.setStatus(_A)
_Dot3MauType25GbaseCRS_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseCRS=_Dot3MauType25GbaseCRS_ObjectIdentity((1,3,6,1,2,1,26,4,89))
if mibBuilder.loadTexts:dot3MauType25GbaseCRS.setStatus(_A)
_Dot3MauType25GbaseKR_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseKR=_Dot3MauType25GbaseKR_ObjectIdentity((1,3,6,1,2,1,26,4,90))
if mibBuilder.loadTexts:dot3MauType25GbaseKR.setStatus(_A)
_Dot3MauType25GbaseKRS_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseKRS=_Dot3MauType25GbaseKRS_ObjectIdentity((1,3,6,1,2,1,26,4,91))
if mibBuilder.loadTexts:dot3MauType25GbaseKRS.setStatus(_A)
_Dot3MauType25GbaseR_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseR=_Dot3MauType25GbaseR_ObjectIdentity((1,3,6,1,2,1,26,4,92))
if mibBuilder.loadTexts:dot3MauType25GbaseR.setStatus(_A)
_Dot3MauType25GbaseSR_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseSR=_Dot3MauType25GbaseSR_ObjectIdentity((1,3,6,1,2,1,26,4,93))
if mibBuilder.loadTexts:dot3MauType25GbaseSR.setStatus(_A)
_Dot3MauType25GbaseT_ObjectIdentity=ObjectIdentity
dot3MauType25GbaseT=_Dot3MauType25GbaseT_ObjectIdentity((1,3,6,1,2,1,26,4,94))
if mibBuilder.loadTexts:dot3MauType25GbaseT.setStatus(_A)
_Dot3MauType40GbaseER4_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseER4=_Dot3MauType40GbaseER4_ObjectIdentity((1,3,6,1,2,1,26,4,95))
if mibBuilder.loadTexts:dot3MauType40GbaseER4.setStatus(_A)
_Dot3MauType40GbaseR_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseR=_Dot3MauType40GbaseR_ObjectIdentity((1,3,6,1,2,1,26,4,96))
if mibBuilder.loadTexts:dot3MauType40GbaseR.setStatus(_A)
_Dot3MauType40GbaseT_ObjectIdentity=ObjectIdentity
dot3MauType40GbaseT=_Dot3MauType40GbaseT_ObjectIdentity((1,3,6,1,2,1,26,4,97))
if mibBuilder.loadTexts:dot3MauType40GbaseT.setStatus(_A)
_Dot3MauType100GbaseCR4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseCR4=_Dot3MauType100GbaseCR4_ObjectIdentity((1,3,6,1,2,1,26,4,98))
if mibBuilder.loadTexts:dot3MauType100GbaseCR4.setStatus(_A)
_Dot3MauType100GbaseKR4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseKR4=_Dot3MauType100GbaseKR4_ObjectIdentity((1,3,6,1,2,1,26,4,99))
if mibBuilder.loadTexts:dot3MauType100GbaseKR4.setStatus(_A)
_Dot3MauType100GbaseKP4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseKP4=_Dot3MauType100GbaseKP4_ObjectIdentity((1,3,6,1,2,1,26,4,100))
if mibBuilder.loadTexts:dot3MauType100GbaseKP4.setStatus(_A)
_Dot3MauType100GbaseR_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseR=_Dot3MauType100GbaseR_ObjectIdentity((1,3,6,1,2,1,26,4,101))
if mibBuilder.loadTexts:dot3MauType100GbaseR.setStatus(_A)
_Dot3MauType100GbaseSR4_ObjectIdentity=ObjectIdentity
dot3MauType100GbaseSR4=_Dot3MauType100GbaseSR4_ObjectIdentity((1,3,6,1,2,1,26,4,102))
if mibBuilder.loadTexts:dot3MauType100GbaseSR4.setStatus(_A)
_Dot3MauType2p5GigT_ObjectIdentity=ObjectIdentity
dot3MauType2p5GigT=_Dot3MauType2p5GigT_ObjectIdentity((1,3,6,1,2,1,26,4,103))
if mibBuilder.loadTexts:dot3MauType2p5GigT.setStatus(_A)
_Dot3MauType5GigT_ObjectIdentity=ObjectIdentity
dot3MauType5GigT=_Dot3MauType5GigT_ObjectIdentity((1,3,6,1,2,1,26,4,104))
if mibBuilder.loadTexts:dot3MauType5GigT.setStatus(_A)
mibBuilder.exportSymbols('IANA-MAU-MIB',**{'IANAifMauTypeListBits':IANAifMauTypeListBits,'IANAifMauMediaAvailable':IANAifMauMediaAvailable,'IANAifMauAutoNegCapBits':IANAifMauAutoNegCapBits,'IANAifJackType':IANAifJackType,'dot3MauType':dot3MauType,'dot3MauTypeAUI':dot3MauTypeAUI,'dot3MauType10Base5':dot3MauType10Base5,'dot3MauTypeFoirl':dot3MauTypeFoirl,'dot3MauType10Base2':dot3MauType10Base2,'dot3MauType10BaseT':dot3MauType10BaseT,'dot3MauType10BaseFP':dot3MauType10BaseFP,'dot3MauType10BaseFB':dot3MauType10BaseFB,'dot3MauType10BaseFL':dot3MauType10BaseFL,'dot3MauType10Broad36':dot3MauType10Broad36,'dot3MauType10BaseTHD':dot3MauType10BaseTHD,'dot3MauType10BaseTFD':dot3MauType10BaseTFD,'dot3MauType10BaseFLHD':dot3MauType10BaseFLHD,'dot3MauType10BaseFLFD':dot3MauType10BaseFLFD,'dot3MauType100BaseT4':dot3MauType100BaseT4,'dot3MauType100BaseTXHD':dot3MauType100BaseTXHD,'dot3MauType100BaseTXFD':dot3MauType100BaseTXFD,'dot3MauType100BaseFXHD':dot3MauType100BaseFXHD,'dot3MauType100BaseFXFD':dot3MauType100BaseFXFD,'dot3MauType100BaseT2HD':dot3MauType100BaseT2HD,'dot3MauType100BaseT2FD':dot3MauType100BaseT2FD,'dot3MauType1000BaseXHD':dot3MauType1000BaseXHD,'dot3MauType1000BaseXFD':dot3MauType1000BaseXFD,'dot3MauType1000BaseLXHD':dot3MauType1000BaseLXHD,'dot3MauType1000BaseLXFD':dot3MauType1000BaseLXFD,'dot3MauType1000BaseSXHD':dot3MauType1000BaseSXHD,'dot3MauType1000BaseSXFD':dot3MauType1000BaseSXFD,'dot3MauType1000BaseCXHD':dot3MauType1000BaseCXHD,'dot3MauType1000BaseCXFD':dot3MauType1000BaseCXFD,'dot3MauType1000BaseTHD':dot3MauType1000BaseTHD,'dot3MauType1000BaseTFD':dot3MauType1000BaseTFD,'dot3MauType10GigBaseX':dot3MauType10GigBaseX,'dot3MauType10GigBaseLX4':dot3MauType10GigBaseLX4,'dot3MauType10GigBaseR':dot3MauType10GigBaseR,'dot3MauType10GigBaseER':dot3MauType10GigBaseER,'dot3MauType10GigBaseLR':dot3MauType10GigBaseLR,'dot3MauType10GigBaseSR':dot3MauType10GigBaseSR,'dot3MauType10GigBaseW':dot3MauType10GigBaseW,'dot3MauType10GigBaseEW':dot3MauType10GigBaseEW,'dot3MauType10GigBaseLW':dot3MauType10GigBaseLW,'dot3MauType10GigBaseSW':dot3MauType10GigBaseSW,'dot3MauType10GigBaseCX4':dot3MauType10GigBaseCX4,'dot3MauType2BaseTL':dot3MauType2BaseTL,'dot3MauType10PassTS':dot3MauType10PassTS,'dot3MauType100BaseBX10D':dot3MauType100BaseBX10D,'dot3MauType100BaseBX10U':dot3MauType100BaseBX10U,'dot3MauType100BaseLX10':dot3MauType100BaseLX10,'dot3MauType1000BaseBX10D':dot3MauType1000BaseBX10D,'dot3MauType1000BaseBX10U':dot3MauType1000BaseBX10U,'dot3MauType1000BaseLX10':dot3MauType1000BaseLX10,'dot3MauType1000BasePX10D':dot3MauType1000BasePX10D,'dot3MauType1000BasePX10U':dot3MauType1000BasePX10U,'dot3MauType1000BasePX20D':dot3MauType1000BasePX20D,'dot3MauType1000BasePX20U':dot3MauType1000BasePX20U,'dot3MauType10GbaseT':dot3MauType10GbaseT,'dot3MauType10GbaseLRM':dot3MauType10GbaseLRM,'dot3MauType1000baseKX':dot3MauType1000baseKX,'dot3MauType10GbaseKX4':dot3MauType10GbaseKX4,'dot3MauType10GbaseKR':dot3MauType10GbaseKR,'dot3MauType10G1GbasePRXD1':dot3MauType10G1GbasePRXD1,'dot3MauType10G1GbasePRXD2':dot3MauType10G1GbasePRXD2,'dot3MauType10G1GbasePRXD3':dot3MauType10G1GbasePRXD3,'dot3MauType10G1GbasePRXU1':dot3MauType10G1GbasePRXU1,'dot3MauType10G1GbasePRXU2':dot3MauType10G1GbasePRXU2,'dot3MauType10G1GbasePRXU3':dot3MauType10G1GbasePRXU3,'dot3MauType10GbasePRD1':dot3MauType10GbasePRD1,'dot3MauType10GbasePRD2':dot3MauType10GbasePRD2,'dot3MauType10GbasePRD3':dot3MauType10GbasePRD3,'dot3MauType10GbasePRU1':dot3MauType10GbasePRU1,'dot3MauType10GbasePRU3':dot3MauType10GbasePRU3,'dot3MauType40GbaseKR4':dot3MauType40GbaseKR4,'dot3MauType40GbaseCR4':dot3MauType40GbaseCR4,'dot3MauType40GbaseSR4':dot3MauType40GbaseSR4,'dot3MauType40GbaseFR':dot3MauType40GbaseFR,'dot3MauType40GbaseLR4':dot3MauType40GbaseLR4,'dot3MauType100GbaseCR10':dot3MauType100GbaseCR10,'dot3MauType100GbaseSR10':dot3MauType100GbaseSR10,'dot3MauType100GbaseLR4':dot3MauType100GbaseLR4,'dot3MauType100GbaseER4':dot3MauType100GbaseER4,'dot3MauType1000baseT1':dot3MauType1000baseT1,'dot3MauType1000basePX30D':dot3MauType1000basePX30D,'dot3MauType1000basePX30U':dot3MauType1000basePX30U,'dot3MauType1000basePX40D':dot3MauType1000basePX40D,'dot3MauType1000basePX40U':dot3MauType1000basePX40U,'dot3MauType10G1GbasePRXD4':dot3MauType10G1GbasePRXD4,'dot3MauType10G1GbasePRXU4':dot3MauType10G1GbasePRXU4,'dot3MauType10GbasePRD4':dot3MauType10GbasePRD4,'dot3MauType10GbasePRU4':dot3MauType10GbasePRU4,'dot3MauType25GbaseCR':dot3MauType25GbaseCR,'dot3MauType25GbaseCRS':dot3MauType25GbaseCRS,'dot3MauType25GbaseKR':dot3MauType25GbaseKR,'dot3MauType25GbaseKRS':dot3MauType25GbaseKRS,'dot3MauType25GbaseR':dot3MauType25GbaseR,'dot3MauType25GbaseSR':dot3MauType25GbaseSR,'dot3MauType25GbaseT':dot3MauType25GbaseT,'dot3MauType40GbaseER4':dot3MauType40GbaseER4,'dot3MauType40GbaseR':dot3MauType40GbaseR,'dot3MauType40GbaseT':dot3MauType40GbaseT,'dot3MauType100GbaseCR4':dot3MauType100GbaseCR4,'dot3MauType100GbaseKR4':dot3MauType100GbaseKR4,'dot3MauType100GbaseKP4':dot3MauType100GbaseKP4,'dot3MauType100GbaseR':dot3MauType100GbaseR,'dot3MauType100GbaseSR4':dot3MauType100GbaseSR4,'dot3MauType2p5GigT':dot3MauType2p5GigT,'dot3MauType5GigT':dot3MauType5GigT,'ianaMauMIB':ianaMauMIB})