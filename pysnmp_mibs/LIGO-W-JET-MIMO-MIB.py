_F='wJetMimoPeerIndex'
_E='LIGO-W-JET-MIMO-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ligoMgmt,=mibBuilder.importSymbols('LIGOWAVE-MIB','ligoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ligoWJetMimoMIB=ModuleIdentity((1,3,6,1,4,1,32750,3,9))
if mibBuilder.loadTexts:ligoWJetMimoMIB.setRevisions(('2010-03-22 00:00',))
_LigoWJetMimoMIBObjects_ObjectIdentity=ObjectIdentity
ligoWJetMimoMIBObjects=_LigoWJetMimoMIBObjects_ObjectIdentity((1,3,6,1,4,1,32750,3,9,1))
_LigoWJetMimoNotifs_ObjectIdentity=ObjectIdentity
ligoWJetMimoNotifs=_LigoWJetMimoNotifs_ObjectIdentity((1,3,6,1,4,1,32750,3,9,1,0))
_LigoWJetMimoInfo_ObjectIdentity=ObjectIdentity
ligoWJetMimoInfo=_LigoWJetMimoInfo_ObjectIdentity((1,3,6,1,4,1,32750,3,9,1,1))
_LigoWJetMimoConf_ObjectIdentity=ObjectIdentity
ligoWJetMimoConf=_LigoWJetMimoConf_ObjectIdentity((1,3,6,1,4,1,32750,3,9,1,2))
_LigoWJetMimoStats_ObjectIdentity=ObjectIdentity
ligoWJetMimoStats=_LigoWJetMimoStats_ObjectIdentity((1,3,6,1,4,1,32750,3,9,1,3))
_WJetMimoStatsTable_Object=MibTable
wJetMimoStatsTable=_WJetMimoStatsTable_Object((1,3,6,1,4,1,32750,3,9,1,3,1))
if mibBuilder.loadTexts:wJetMimoStatsTable.setStatus(_A)
_WJetMimoStatsEntry_Object=MibTableRow
wJetMimoStatsEntry=_WJetMimoStatsEntry_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1))
wJetMimoStatsEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:wJetMimoStatsEntry.setStatus(_A)
_WJetMimoPeerIndex_Type=Integer32
_WJetMimoPeerIndex_Object=MibTableColumn
wJetMimoPeerIndex=_WJetMimoPeerIndex_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,1),_WJetMimoPeerIndex_Type())
wJetMimoPeerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wJetMimoPeerIndex.setStatus(_A)
_WJetMimoMacAddress_Type=MacAddress
_WJetMimoMacAddress_Object=MibTableColumn
wJetMimoMacAddress=_WJetMimoMacAddress_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,2),_WJetMimoMacAddress_Type())
wJetMimoMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoMacAddress.setStatus(_A)
_WJetMimoTxTokens_Type=Counter32
_WJetMimoTxTokens_Object=MibTableColumn
wJetMimoTxTokens=_WJetMimoTxTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,3),_WJetMimoTxTokens_Type())
wJetMimoTxTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoTxTokens.setStatus(_A)
_WJetMimoRxTokens_Type=Counter32
_WJetMimoRxTokens_Object=MibTableColumn
wJetMimoRxTokens=_WJetMimoRxTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,4),_WJetMimoRxTokens_Type())
wJetMimoRxTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoRxTokens.setStatus(_A)
_WJetMimoDupTokens_Type=Counter32
_WJetMimoDupTokens_Object=MibTableColumn
wJetMimoDupTokens=_WJetMimoDupTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,5),_WJetMimoDupTokens_Type())
wJetMimoDupTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoDupTokens.setStatus(_A)
_WJetMimoLostTokens_Type=Counter32
_WJetMimoLostTokens_Object=MibTableColumn
wJetMimoLostTokens=_WJetMimoLostTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,6),_WJetMimoLostTokens_Type())
wJetMimoLostTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoLostTokens.setStatus(_A)
_WJetMimoDroppedTokens_Type=Counter32
_WJetMimoDroppedTokens_Object=MibTableColumn
wJetMimoDroppedTokens=_WJetMimoDroppedTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,7),_WJetMimoDroppedTokens_Type())
wJetMimoDroppedTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoDroppedTokens.setStatus(_A)
_WJetMimoTxFailures_Type=Counter32
_WJetMimoTxFailures_Object=MibTableColumn
wJetMimoTxFailures=_WJetMimoTxFailures_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,8),_WJetMimoTxFailures_Type())
wJetMimoTxFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoTxFailures.setStatus(_A)
_WJetMimoReinjectedTokens_Type=Counter32
_WJetMimoReinjectedTokens_Object=MibTableColumn
wJetMimoReinjectedTokens=_WJetMimoReinjectedTokens_Object((1,3,6,1,4,1,32750,3,9,1,3,1,1,9),_WJetMimoReinjectedTokens_Type())
wJetMimoReinjectedTokens.setMaxAccess(_B)
if mibBuilder.loadTexts:wJetMimoReinjectedTokens.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ligoWJetMimoMIB':ligoWJetMimoMIB,'ligoWJetMimoMIBObjects':ligoWJetMimoMIBObjects,'ligoWJetMimoNotifs':ligoWJetMimoNotifs,'ligoWJetMimoInfo':ligoWJetMimoInfo,'ligoWJetMimoConf':ligoWJetMimoConf,'ligoWJetMimoStats':ligoWJetMimoStats,'wJetMimoStatsTable':wJetMimoStatsTable,'wJetMimoStatsEntry':wJetMimoStatsEntry,_F:wJetMimoPeerIndex,'wJetMimoMacAddress':wJetMimoMacAddress,'wJetMimoTxTokens':wJetMimoTxTokens,'wJetMimoRxTokens':wJetMimoRxTokens,'wJetMimoDupTokens':wJetMimoDupTokens,'wJetMimoLostTokens':wJetMimoLostTokens,'wJetMimoDroppedTokens':wJetMimoDroppedTokens,'wJetMimoTxFailures':wJetMimoTxFailures,'wJetMimoReinjectedTokens':wJetMimoReinjectedTokens})