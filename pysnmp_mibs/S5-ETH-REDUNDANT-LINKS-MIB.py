_I='s5EnRedPortPortIndx'
_H='s5EnRedPortBrdIndx'
_G='TimeIntervalSec'
_F='other'
_E='S5-ETH-REDUNDANT-LINKS-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5EnCfg,=mibBuilder.importSymbols('S5-ETHERNET-MIB','s5EnCfg')
TimeIntervalSec,=mibBuilder.importSymbols('S5-TCS-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
s5EthRedundantLinksMib2=ModuleIdentity((1,3,6,1,4,1,45,1,6,6,1,99))
if mibBuilder.loadTexts:s5EthRedundantLinksMib2.setRevisions(('2004-11-03 00:00','2004-07-20 00:00'))
_S5EnRedun_ObjectIdentity=ObjectIdentity
s5EnRedun=_S5EnRedun_ObjectIdentity((1,3,6,1,4,1,45,1,6,6,1,2))
_S5EnRedPortTable_Object=MibTable
s5EnRedPortTable=_S5EnRedPortTable_Object((1,3,6,1,4,1,45,1,6,6,1,2,1))
if mibBuilder.loadTexts:s5EnRedPortTable.setStatus(_A)
_S5EnRedPortEntry_Object=MibTableRow
s5EnRedPortEntry=_S5EnRedPortEntry_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1))
s5EnRedPortEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:s5EnRedPortEntry.setStatus(_A)
class _S5EnRedPortBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnRedPortBrdIndx_Type.__name__=_B
_S5EnRedPortBrdIndx_Object=MibTableColumn
s5EnRedPortBrdIndx=_S5EnRedPortBrdIndx_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,1),_S5EnRedPortBrdIndx_Type())
s5EnRedPortBrdIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortBrdIndx.setStatus(_A)
class _S5EnRedPortPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnRedPortPortIndx_Type.__name__=_B
_S5EnRedPortPortIndx_Object=MibTableColumn
s5EnRedPortPortIndx=_S5EnRedPortPortIndx_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,2),_S5EnRedPortPortIndx_Type())
s5EnRedPortPortIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortPortIndx.setStatus(_A)
class _S5EnRedPortCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hwRedOnly',1),('swRedOnly',2),('hwAndSwRed',3)))
_S5EnRedPortCapability_Type.__name__=_B
_S5EnRedPortCapability_Object=MibTableColumn
s5EnRedPortCapability=_S5EnRedPortCapability_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,3),_S5EnRedPortCapability_Type())
s5EnRedPortCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortCapability.setStatus(_A)
class _S5EnRedPortRedundMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('standAlone',1),('hwActive',2),('hwStandby',3),('swActive',4),('swStandby',5)))
_S5EnRedPortRedundMode_Type.__name__=_B
_S5EnRedPortRedundMode_Object=MibTableColumn
s5EnRedPortRedundMode=_S5EnRedPortRedundMode_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,4),_S5EnRedPortRedundMode_Type())
s5EnRedPortRedundMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortRedundMode.setStatus(_A)
class _S5EnRedPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),('localFault',3),('remoteFault',4)))
_S5EnRedPortOperStatus_Type.__name__=_B
_S5EnRedPortOperStatus_Object=MibTableColumn
s5EnRedPortOperStatus=_S5EnRedPortOperStatus_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,5),_S5EnRedPortOperStatus_Type())
s5EnRedPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortOperStatus.setStatus(_A)
class _S5EnRedPortRemoteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('snpxFLRemFltCpblPortUp',1),('snpxFLFBRemFltCpblPortUp',2),('tenBaseTFLPortUp',3),('tenBaseFBPortUp',4),('snpxRemFltCpblPortFault',5),('tenBaseFBPortFault',6),('unknown',7)))
_S5EnRedPortRemoteOperStatus_Type.__name__=_B
_S5EnRedPortRemoteOperStatus_Object=MibTableColumn
s5EnRedPortRemoteOperStatus=_S5EnRedPortRemoteOperStatus_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,6),_S5EnRedPortRemoteOperStatus_Type())
s5EnRedPortRemoteOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortRemoteOperStatus.setStatus(_A)
class _S5EnRedPortRemFltSelectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('synoptics',1),('standard',2)))
_S5EnRedPortRemFltSelectMode_Type.__name__=_B
_S5EnRedPortRemFltSelectMode_Object=MibTableColumn
s5EnRedPortRemFltSelectMode=_S5EnRedPortRemFltSelectMode_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,7),_S5EnRedPortRemFltSelectMode_Type())
s5EnRedPortRemFltSelectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortRemFltSelectMode.setStatus(_A)
class _S5EnRedPortTxMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('autoCfg',1),('fl',2),('fb',3),(_F,4)))
_S5EnRedPortTxMode_Type.__name__=_B
_S5EnRedPortTxMode_Object=MibTableColumn
s5EnRedPortTxMode=_S5EnRedPortTxMode_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,8),_S5EnRedPortTxMode_Type())
s5EnRedPortTxMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortTxMode.setStatus(_A)
_S5EnRedPortFaults_Type=Counter32
_S5EnRedPortFaults_Object=MibTableColumn
s5EnRedPortFaults=_S5EnRedPortFaults_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,9),_S5EnRedPortFaults_Type())
s5EnRedPortFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortFaults.setStatus(_A)
_S5EnRedPortModeChanges_Type=Counter32
_S5EnRedPortModeChanges_Object=MibTableColumn
s5EnRedPortModeChanges=_S5EnRedPortModeChanges_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,10),_S5EnRedPortModeChanges_Type())
s5EnRedPortModeChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedPortModeChanges.setStatus(_A)
class _S5EnRedPortCompanionBrdNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnRedPortCompanionBrdNum_Type.__name__=_B
_S5EnRedPortCompanionBrdNum_Object=MibTableColumn
s5EnRedPortCompanionBrdNum=_S5EnRedPortCompanionBrdNum_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,11),_S5EnRedPortCompanionBrdNum_Type())
s5EnRedPortCompanionBrdNum.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortCompanionBrdNum.setStatus(_A)
class _S5EnRedPortCompanionPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnRedPortCompanionPortNum_Type.__name__=_B
_S5EnRedPortCompanionPortNum_Object=MibTableColumn
s5EnRedPortCompanionPortNum=_S5EnRedPortCompanionPortNum_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,12),_S5EnRedPortCompanionPortNum_Type())
s5EnRedPortCompanionPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortCompanionPortNum.setStatus(_A)
class _S5EnRedPortSwitchoverStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('timedSwitchover',2)))
_S5EnRedPortSwitchoverStatus_Type.__name__=_B
_S5EnRedPortSwitchoverStatus_Object=MibTableColumn
s5EnRedPortSwitchoverStatus=_S5EnRedPortSwitchoverStatus_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,13),_S5EnRedPortSwitchoverStatus_Type())
s5EnRedPortSwitchoverStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortSwitchoverStatus.setStatus(_A)
class _S5EnRedPortSwitchoverTime_Type(TimeIntervalSec):subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_S5EnRedPortSwitchoverTime_Type.__name__=_G
_S5EnRedPortSwitchoverTime_Object=MibTableColumn
s5EnRedPortSwitchoverTime=_S5EnRedPortSwitchoverTime_Object((1,3,6,1,4,1,45,1,6,6,1,2,1,1,14),_S5EnRedPortSwitchoverTime_Type())
s5EnRedPortSwitchoverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnRedPortSwitchoverTime.setStatus(_A)
_S5EnRedLastChg_Type=TimeTicks
_S5EnRedLastChg_Object=MibScalar
s5EnRedLastChg=_S5EnRedLastChg_Object((1,3,6,1,4,1,45,1,6,6,1,2,2),_S5EnRedLastChg_Type())
s5EnRedLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:s5EnRedLastChg.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'s5EnRedun':s5EnRedun,'s5EnRedPortTable':s5EnRedPortTable,'s5EnRedPortEntry':s5EnRedPortEntry,_H:s5EnRedPortBrdIndx,_I:s5EnRedPortPortIndx,'s5EnRedPortCapability':s5EnRedPortCapability,'s5EnRedPortRedundMode':s5EnRedPortRedundMode,'s5EnRedPortOperStatus':s5EnRedPortOperStatus,'s5EnRedPortRemoteOperStatus':s5EnRedPortRemoteOperStatus,'s5EnRedPortRemFltSelectMode':s5EnRedPortRemFltSelectMode,'s5EnRedPortTxMode':s5EnRedPortTxMode,'s5EnRedPortFaults':s5EnRedPortFaults,'s5EnRedPortModeChanges':s5EnRedPortModeChanges,'s5EnRedPortCompanionBrdNum':s5EnRedPortCompanionBrdNum,'s5EnRedPortCompanionPortNum':s5EnRedPortCompanionPortNum,'s5EnRedPortSwitchoverStatus':s5EnRedPortSwitchoverStatus,'s5EnRedPortSwitchoverTime':s5EnRedPortSwitchoverTime,'s5EnRedLastChg':s5EnRedLastChg,'s5EthRedundantLinksMib2':s5EthRedundantLinksMib2})