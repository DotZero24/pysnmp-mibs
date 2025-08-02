_N='a3IPsecureAuthOutFlags'
_M='a3IPsecureAuthOutPort'
_L='a3IPsecureAuthInFlags'
_K='a3IPsecureAuthInPort'
_J='a3IPsecureParamPortIndex'
_I='unclassified'
_H='confidential'
_G='secret'
_F='topSecret'
_E='read-only'
_D='A3Com-IPSO-r1-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_A3ComIPSO_ObjectIdentity=ObjectIdentity
a3ComIPSO=_A3ComIPSO_ObjectIdentity((1,3,6,1,4,1,43,2,12))
class _A3IPsecureCtl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('security1108',1),('security1038',2),('noSecurity',3)))
_A3IPsecureCtl_Type.__name__=_C
_A3IPsecureCtl_Object=MibScalar
a3IPsecureCtl=_A3IPsecureCtl_Object((1,3,6,1,4,1,43,2,12,1),_A3IPsecureCtl_Type())
a3IPsecureCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureCtl.setStatus(_A)
class _A3IPsecureFileServer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_A3IPsecureFileServer_Type.__name__=_C
_A3IPsecureFileServer_Object=MibScalar
a3IPsecureFileServer=_A3IPsecureFileServer_Object((1,3,6,1,4,1,43,2,12,2),_A3IPsecureFileServer_Type())
a3IPsecureFileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureFileServer.setStatus(_A)
_A3IPsecureParamTable_Object=MibTable
a3IPsecureParamTable=_A3IPsecureParamTable_Object((1,3,6,1,4,1,43,2,12,3))
if mibBuilder.loadTexts:a3IPsecureParamTable.setStatus(_A)
_A3IPsecureParamEntry_Object=MibTableRow
a3IPsecureParamEntry=_A3IPsecureParamEntry_Object((1,3,6,1,4,1,43,2,12,3,1))
a3IPsecureParamEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:a3IPsecureParamEntry.setStatus(_A)
_A3IPsecureParamPortIndex_Type=Integer32
_A3IPsecureParamPortIndex_Object=MibTableColumn
a3IPsecureParamPortIndex=_A3IPsecureParamPortIndex_Object((1,3,6,1,4,1,43,2,12,3,1,1),_A3IPsecureParamPortIndex_Type())
a3IPsecureParamPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsecureParamPortIndex.setStatus(_A)
class _A3IPsecureParamCtl_Type(Integer32):defaultValue=0
_A3IPsecureParamCtl_Type.__name__=_C
_A3IPsecureParamCtl_Object=MibTableColumn
a3IPsecureParamCtl=_A3IPsecureParamCtl_Object((1,3,6,1,4,1,43,2,12,3,1,2),_A3IPsecureParamCtl_Type())
a3IPsecureParamCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureParamCtl.setStatus(_A)
class _A3IPsecureLabelDefaultLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),(_F,2),(_G,3),(_H,4),(_I,5)))
_A3IPsecureLabelDefaultLevel_Type.__name__=_C
_A3IPsecureLabelDefaultLevel_Object=MibTableColumn
a3IPsecureLabelDefaultLevel=_A3IPsecureLabelDefaultLevel_Object((1,3,6,1,4,1,43,2,12,3,1,3),_A3IPsecureLabelDefaultLevel_Type())
a3IPsecureLabelDefaultLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureLabelDefaultLevel.setStatus(_A)
class _A3IPsecureLabelDefaultAuth_Type(Integer32):defaultValue=0
_A3IPsecureLabelDefaultAuth_Type.__name__=_C
_A3IPsecureLabelDefaultAuth_Object=MibTableColumn
a3IPsecureLabelDefaultAuth=_A3IPsecureLabelDefaultAuth_Object((1,3,6,1,4,1,43,2,12,3,1,4),_A3IPsecureLabelDefaultAuth_Type())
a3IPsecureLabelDefaultAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureLabelDefaultAuth.setStatus(_A)
class _A3IPsecureLabelSysLevel_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),(_F,2),(_G,3),(_H,4),(_I,5)))
_A3IPsecureLabelSysLevel_Type.__name__=_C
_A3IPsecureLabelSysLevel_Object=MibTableColumn
a3IPsecureLabelSysLevel=_A3IPsecureLabelSysLevel_Object((1,3,6,1,4,1,43,2,12,3,1,5),_A3IPsecureLabelSysLevel_Type())
a3IPsecureLabelSysLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureLabelSysLevel.setStatus(_A)
class _A3IPsecureLabelSysAuth_Type(Integer32):defaultValue=128
_A3IPsecureLabelSysAuth_Type.__name__=_C
_A3IPsecureLabelSysAuth_Object=MibTableColumn
a3IPsecureLabelSysAuth=_A3IPsecureLabelSysAuth_Object((1,3,6,1,4,1,43,2,12,3,1,6),_A3IPsecureLabelSysAuth_Type())
a3IPsecureLabelSysAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureLabelSysAuth.setStatus(_A)
class _A3IPsecureMinLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_A3IPsecureMinLevel_Type.__name__=_C
_A3IPsecureMinLevel_Object=MibTableColumn
a3IPsecureMinLevel=_A3IPsecureMinLevel_Object((1,3,6,1,4,1,43,2,12,3,1,7),_A3IPsecureMinLevel_Type())
a3IPsecureMinLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureMinLevel.setStatus(_A)
class _A3IPsecureMaxLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_A3IPsecureMaxLevel_Type.__name__=_C
_A3IPsecureMaxLevel_Object=MibTableColumn
a3IPsecureMaxLevel=_A3IPsecureMaxLevel_Object((1,3,6,1,4,1,43,2,12,3,1,8),_A3IPsecureMaxLevel_Type())
a3IPsecureMaxLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureMaxLevel.setStatus(_A)
_A3IPsecureAuthInTable_Object=MibTable
a3IPsecureAuthInTable=_A3IPsecureAuthInTable_Object((1,3,6,1,4,1,43,2,12,4))
if mibBuilder.loadTexts:a3IPsecureAuthInTable.setStatus(_A)
_A3IPsecureAuthInEntry_Object=MibTableRow
a3IPsecureAuthInEntry=_A3IPsecureAuthInEntry_Object((1,3,6,1,4,1,43,2,12,4,1))
a3IPsecureAuthInEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:a3IPsecureAuthInEntry.setStatus(_A)
_A3IPsecureAuthInPort_Type=Integer32
_A3IPsecureAuthInPort_Object=MibTableColumn
a3IPsecureAuthInPort=_A3IPsecureAuthInPort_Object((1,3,6,1,4,1,43,2,12,4,1,1),_A3IPsecureAuthInPort_Type())
a3IPsecureAuthInPort.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsecureAuthInPort.setStatus(_A)
_A3IPsecureAuthInFlags_Type=Integer32
_A3IPsecureAuthInFlags_Object=MibTableColumn
a3IPsecureAuthInFlags=_A3IPsecureAuthInFlags_Object((1,3,6,1,4,1,43,2,12,4,1,2),_A3IPsecureAuthInFlags_Type())
a3IPsecureAuthInFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsecureAuthInFlags.setStatus(_A)
class _A3IPsecureAuthInMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('any',2)))
_A3IPsecureAuthInMatch_Type.__name__=_C
_A3IPsecureAuthInMatch_Object=MibTableColumn
a3IPsecureAuthInMatch=_A3IPsecureAuthInMatch_Object((1,3,6,1,4,1,43,2,12,4,1,3),_A3IPsecureAuthInMatch_Type())
a3IPsecureAuthInMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureAuthInMatch.setStatus(_A)
_A3IPsecureAuthInStatus_Type=RowStatus
_A3IPsecureAuthInStatus_Object=MibTableColumn
a3IPsecureAuthInStatus=_A3IPsecureAuthInStatus_Object((1,3,6,1,4,1,43,2,12,4,1,4),_A3IPsecureAuthInStatus_Type())
a3IPsecureAuthInStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureAuthInStatus.setStatus(_A)
_A3IPsecureAuthOutTable_Object=MibTable
a3IPsecureAuthOutTable=_A3IPsecureAuthOutTable_Object((1,3,6,1,4,1,43,2,12,5))
if mibBuilder.loadTexts:a3IPsecureAuthOutTable.setStatus(_A)
_A3IPsecureAuthOutEntry_Object=MibTableRow
a3IPsecureAuthOutEntry=_A3IPsecureAuthOutEntry_Object((1,3,6,1,4,1,43,2,12,5,1))
a3IPsecureAuthOutEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:a3IPsecureAuthOutEntry.setStatus(_A)
_A3IPsecureAuthOutPort_Type=Integer32
_A3IPsecureAuthOutPort_Object=MibTableColumn
a3IPsecureAuthOutPort=_A3IPsecureAuthOutPort_Object((1,3,6,1,4,1,43,2,12,5,1,1),_A3IPsecureAuthOutPort_Type())
a3IPsecureAuthOutPort.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsecureAuthOutPort.setStatus(_A)
_A3IPsecureAuthOutFlags_Type=Integer32
_A3IPsecureAuthOutFlags_Object=MibTableColumn
a3IPsecureAuthOutFlags=_A3IPsecureAuthOutFlags_Object((1,3,6,1,4,1,43,2,12,5,1,2),_A3IPsecureAuthOutFlags_Type())
a3IPsecureAuthOutFlags.setMaxAccess(_E)
if mibBuilder.loadTexts:a3IPsecureAuthOutFlags.setStatus(_A)
class _A3IPsecureAuthOutMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('any',2)))
_A3IPsecureAuthOutMatch_Type.__name__=_C
_A3IPsecureAuthOutMatch_Object=MibTableColumn
a3IPsecureAuthOutMatch=_A3IPsecureAuthOutMatch_Object((1,3,6,1,4,1,43,2,12,5,1,3),_A3IPsecureAuthOutMatch_Type())
a3IPsecureAuthOutMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureAuthOutMatch.setStatus(_A)
_A3IPsecureAuthOutStatus_Type=RowStatus
_A3IPsecureAuthOutStatus_Object=MibTableColumn
a3IPsecureAuthOutStatus=_A3IPsecureAuthOutStatus_Object((1,3,6,1,4,1,43,2,12,5,1,4),_A3IPsecureAuthOutStatus_Type())
a3IPsecureAuthOutStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3IPsecureAuthOutStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RowStatus':RowStatus,'a3Com':a3Com,'brouterMIB':brouterMIB,'a3ComIPSO':a3ComIPSO,'a3IPsecureCtl':a3IPsecureCtl,'a3IPsecureFileServer':a3IPsecureFileServer,'a3IPsecureParamTable':a3IPsecureParamTable,'a3IPsecureParamEntry':a3IPsecureParamEntry,_J:a3IPsecureParamPortIndex,'a3IPsecureParamCtl':a3IPsecureParamCtl,'a3IPsecureLabelDefaultLevel':a3IPsecureLabelDefaultLevel,'a3IPsecureLabelDefaultAuth':a3IPsecureLabelDefaultAuth,'a3IPsecureLabelSysLevel':a3IPsecureLabelSysLevel,'a3IPsecureLabelSysAuth':a3IPsecureLabelSysAuth,'a3IPsecureMinLevel':a3IPsecureMinLevel,'a3IPsecureMaxLevel':a3IPsecureMaxLevel,'a3IPsecureAuthInTable':a3IPsecureAuthInTable,'a3IPsecureAuthInEntry':a3IPsecureAuthInEntry,_K:a3IPsecureAuthInPort,_L:a3IPsecureAuthInFlags,'a3IPsecureAuthInMatch':a3IPsecureAuthInMatch,'a3IPsecureAuthInStatus':a3IPsecureAuthInStatus,'a3IPsecureAuthOutTable':a3IPsecureAuthOutTable,'a3IPsecureAuthOutEntry':a3IPsecureAuthOutEntry,_M:a3IPsecureAuthOutPort,_N:a3IPsecureAuthOutFlags,'a3IPsecureAuthOutMatch':a3IPsecureAuthOutMatch,'a3IPsecureAuthOutStatus':a3IPsecureAuthOutStatus})