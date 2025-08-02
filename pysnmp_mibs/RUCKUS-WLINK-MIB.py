_M='ruckusWLINKIIStaIndex'
_L='notAvailable'
_K='notDecided'
_J='nonRootBridge'
_I='rootBridge'
_H='ruckusWLINKIndex'
_G='ifIndex'
_F='IF-MIB'
_E='RUCKUS-WLINK-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
ruckusCommonWLINKModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonWLINKModule')
RuckusSSID,=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusSSID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
ruckusWLINKMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,15,1))
_RuckusWLINKObjects_ObjectIdentity=ObjectIdentity
ruckusWLINKObjects=_RuckusWLINKObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,15,1,1))
_RuckusWLINKInfo_ObjectIdentity=ObjectIdentity
ruckusWLINKInfo=_RuckusWLINKInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,15,1,1,1))
_RuckusWLINKTable_Object=MibTable
ruckusWLINKTable=_RuckusWLINKTable_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1))
if mibBuilder.loadTexts:ruckusWLINKTable.setStatus(_A)
_RuckusWLINKEntry_Object=MibTableRow
ruckusWLINKEntry=_RuckusWLINKEntry_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1))
ruckusWLINKEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ruckusWLINKEntry.setStatus(_A)
_RuckusWLINKSSID_Type=RuckusSSID
_RuckusWLINKSSID_Object=MibTableColumn
ruckusWLINKSSID=_RuckusWLINKSSID_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,1),_RuckusWLINKSSID_Type())
ruckusWLINKSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKSSID.setStatus(_A)
class _RuckusWLINKRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_RuckusWLINKRole_Type.__name__=_C
_RuckusWLINKRole_Object=MibTableColumn
ruckusWLINKRole=_RuckusWLINKRole_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,2),_RuckusWLINKRole_Type())
ruckusWLINKRole.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKRole.setStatus(_A)
_RuckusWLINKLocalMAC_Type=MacAddress
_RuckusWLINKLocalMAC_Object=MibTableColumn
ruckusWLINKLocalMAC=_RuckusWLINKLocalMAC_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,3),_RuckusWLINKLocalMAC_Type())
ruckusWLINKLocalMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKLocalMAC.setStatus(_A)
_RuckusWLINKRemoteMAC_Type=MacAddress
_RuckusWLINKRemoteMAC_Object=MibTableColumn
ruckusWLINKRemoteMAC=_RuckusWLINKRemoteMAC_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,4),_RuckusWLINKRemoteMAC_Type())
ruckusWLINKRemoteMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKRemoteMAC.setStatus(_A)
_RuckusWLINKTxPkts_Type=Counter32
_RuckusWLINKTxPkts_Object=MibTableColumn
ruckusWLINKTxPkts=_RuckusWLINKTxPkts_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,5),_RuckusWLINKTxPkts_Type())
ruckusWLINKTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKTxPkts.setStatus(_A)
_RuckusWLINKTxBytes_Type=Counter32
_RuckusWLINKTxBytes_Object=MibTableColumn
ruckusWLINKTxBytes=_RuckusWLINKTxBytes_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,6),_RuckusWLINKTxBytes_Type())
ruckusWLINKTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKTxBytes.setStatus(_A)
_RuckusWLINKRxPkts_Type=Counter32
_RuckusWLINKRxPkts_Object=MibTableColumn
ruckusWLINKRxPkts=_RuckusWLINKRxPkts_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,7),_RuckusWLINKRxPkts_Type())
ruckusWLINKRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKRxPkts.setStatus(_A)
_RuckusWLINKRxBytes_Type=Counter32
_RuckusWLINKRxBytes_Object=MibTableColumn
ruckusWLINKRxBytes=_RuckusWLINKRxBytes_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,8),_RuckusWLINKRxBytes_Type())
ruckusWLINKRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKRxBytes.setStatus(_A)
class _RuckusWLINKEstablishTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusWLINKEstablishTime_Type.__name__=_D
_RuckusWLINKEstablishTime_Object=MibTableColumn
ruckusWLINKEstablishTime=_RuckusWLINKEstablishTime_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,9),_RuckusWLINKEstablishTime_Type())
ruckusWLINKEstablishTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKEstablishTime.setStatus(_A)
_RuckusWLINKUpTime_Type=Unsigned32
_RuckusWLINKUpTime_Object=MibTableColumn
ruckusWLINKUpTime=_RuckusWLINKUpTime_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,10),_RuckusWLINKUpTime_Type())
ruckusWLINKUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKUpTime.setStatus(_A)
_RuckusWLINKRssi_Type=Integer32
_RuckusWLINKRssi_Object=MibTableColumn
ruckusWLINKRssi=_RuckusWLINKRssi_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,11),_RuckusWLINKRssi_Type())
ruckusWLINKRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKRssi.setStatus(_A)
_RuckusWLINKUpCount_Type=Integer32
_RuckusWLINKUpCount_Object=MibTableColumn
ruckusWLINKUpCount=_RuckusWLINKUpCount_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,12),_RuckusWLINKUpCount_Type())
ruckusWLINKUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKUpCount.setStatus(_A)
_RuckusWLINKDownCount_Type=Integer32
_RuckusWLINKDownCount_Object=MibTableColumn
ruckusWLINKDownCount=_RuckusWLINKDownCount_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,13),_RuckusWLINKDownCount_Type())
ruckusWLINKDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKDownCount.setStatus(_A)
_RuckusWLINKIndex_Type=InterfaceIndex
_RuckusWLINKIndex_Object=MibTableColumn
ruckusWLINKIndex=_RuckusWLINKIndex_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,1,1,200),_RuckusWLINKIndex_Type())
ruckusWLINKIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIndex.setStatus(_A)
_RuckusWLINKIITable_Object=MibTable
ruckusWLINKIITable=_RuckusWLINKIITable_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2))
if mibBuilder.loadTexts:ruckusWLINKIITable.setStatus(_A)
_RuckusWLINKIIEntry_Object=MibTableRow
ruckusWLINKIIEntry=_RuckusWLINKIIEntry_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1))
ruckusWLINKIIEntry.setIndexNames((0,_F,_G),(0,_E,_M))
if mibBuilder.loadTexts:ruckusWLINKIIEntry.setStatus(_A)
_RuckusWLINKIIStaIndex_Type=Integer32
_RuckusWLINKIIStaIndex_Object=MibTableColumn
ruckusWLINKIIStaIndex=_RuckusWLINKIIStaIndex_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,1),_RuckusWLINKIIStaIndex_Type())
ruckusWLINKIIStaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIStaIndex.setStatus(_A)
_RuckusWLINKIISSID_Type=RuckusSSID
_RuckusWLINKIISSID_Object=MibTableColumn
ruckusWLINKIISSID=_RuckusWLINKIISSID_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,2),_RuckusWLINKIISSID_Type())
ruckusWLINKIISSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIISSID.setStatus(_A)
class _RuckusWLINKIIRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_RuckusWLINKIIRole_Type.__name__=_C
_RuckusWLINKIIRole_Object=MibTableColumn
ruckusWLINKIIRole=_RuckusWLINKIIRole_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,3),_RuckusWLINKIIRole_Type())
ruckusWLINKIIRole.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIRole.setStatus(_A)
_RuckusWLINKIILocalMAC_Type=MacAddress
_RuckusWLINKIILocalMAC_Object=MibTableColumn
ruckusWLINKIILocalMAC=_RuckusWLINKIILocalMAC_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,4),_RuckusWLINKIILocalMAC_Type())
ruckusWLINKIILocalMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIILocalMAC.setStatus(_A)
_RuckusWLINKIIRemoteMAC_Type=MacAddress
_RuckusWLINKIIRemoteMAC_Object=MibTableColumn
ruckusWLINKIIRemoteMAC=_RuckusWLINKIIRemoteMAC_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,5),_RuckusWLINKIIRemoteMAC_Type())
ruckusWLINKIIRemoteMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIRemoteMAC.setStatus(_A)
_RuckusWLINKIITxPkts_Type=Counter32
_RuckusWLINKIITxPkts_Object=MibTableColumn
ruckusWLINKIITxPkts=_RuckusWLINKIITxPkts_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,6),_RuckusWLINKIITxPkts_Type())
ruckusWLINKIITxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIITxPkts.setStatus(_A)
_RuckusWLINKIITxBytes_Type=Counter32
_RuckusWLINKIITxBytes_Object=MibTableColumn
ruckusWLINKIITxBytes=_RuckusWLINKIITxBytes_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,7),_RuckusWLINKIITxBytes_Type())
ruckusWLINKIITxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIITxBytes.setStatus(_A)
_RuckusWLINKIIRxPkts_Type=Counter32
_RuckusWLINKIIRxPkts_Object=MibTableColumn
ruckusWLINKIIRxPkts=_RuckusWLINKIIRxPkts_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,8),_RuckusWLINKIIRxPkts_Type())
ruckusWLINKIIRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIRxPkts.setStatus(_A)
_RuckusWLINKIIRxBytes_Type=Counter32
_RuckusWLINKIIRxBytes_Object=MibTableColumn
ruckusWLINKIIRxBytes=_RuckusWLINKIIRxBytes_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,9),_RuckusWLINKIIRxBytes_Type())
ruckusWLINKIIRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIRxBytes.setStatus(_A)
class _RuckusWLINKIIEstablishTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusWLINKIIEstablishTime_Type.__name__=_D
_RuckusWLINKIIEstablishTime_Object=MibTableColumn
ruckusWLINKIIEstablishTime=_RuckusWLINKIIEstablishTime_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,10),_RuckusWLINKIIEstablishTime_Type())
ruckusWLINKIIEstablishTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIEstablishTime.setStatus(_A)
_RuckusWLINKIIUpTime_Type=Unsigned32
_RuckusWLINKIIUpTime_Object=MibTableColumn
ruckusWLINKIIUpTime=_RuckusWLINKIIUpTime_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,11),_RuckusWLINKIIUpTime_Type())
ruckusWLINKIIUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIUpTime.setStatus(_A)
_RuckusWLINKIIRssi_Type=Integer32
_RuckusWLINKIIRssi_Object=MibTableColumn
ruckusWLINKIIRssi=_RuckusWLINKIIRssi_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,12),_RuckusWLINKIIRssi_Type())
ruckusWLINKIIRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIRssi.setStatus(_A)
_RuckusWLINKIIUpCount_Type=Integer32
_RuckusWLINKIIUpCount_Object=MibTableColumn
ruckusWLINKIIUpCount=_RuckusWLINKIIUpCount_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,13),_RuckusWLINKIIUpCount_Type())
ruckusWLINKIIUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIUpCount.setStatus(_A)
_RuckusWLINKIIDownCount_Type=Integer32
_RuckusWLINKIIDownCount_Object=MibTableColumn
ruckusWLINKIIDownCount=_RuckusWLINKIIDownCount_Object((1,3,6,1,4,1,25053,1,1,15,1,1,1,2,1,14),_RuckusWLINKIIDownCount_Type())
ruckusWLINKIIDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusWLINKIIDownCount.setStatus(_A)
_RuckusWLINKEvents_ObjectIdentity=ObjectIdentity
ruckusWLINKEvents=_RuckusWLINKEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,15,1,2))
mibBuilder.exportSymbols(_E,**{'ruckusWLINKMIB':ruckusWLINKMIB,'ruckusWLINKObjects':ruckusWLINKObjects,'ruckusWLINKInfo':ruckusWLINKInfo,'ruckusWLINKTable':ruckusWLINKTable,'ruckusWLINKEntry':ruckusWLINKEntry,'ruckusWLINKSSID':ruckusWLINKSSID,'ruckusWLINKRole':ruckusWLINKRole,'ruckusWLINKLocalMAC':ruckusWLINKLocalMAC,'ruckusWLINKRemoteMAC':ruckusWLINKRemoteMAC,'ruckusWLINKTxPkts':ruckusWLINKTxPkts,'ruckusWLINKTxBytes':ruckusWLINKTxBytes,'ruckusWLINKRxPkts':ruckusWLINKRxPkts,'ruckusWLINKRxBytes':ruckusWLINKRxBytes,'ruckusWLINKEstablishTime':ruckusWLINKEstablishTime,'ruckusWLINKUpTime':ruckusWLINKUpTime,'ruckusWLINKRssi':ruckusWLINKRssi,'ruckusWLINKUpCount':ruckusWLINKUpCount,'ruckusWLINKDownCount':ruckusWLINKDownCount,_H:ruckusWLINKIndex,'ruckusWLINKIITable':ruckusWLINKIITable,'ruckusWLINKIIEntry':ruckusWLINKIIEntry,_M:ruckusWLINKIIStaIndex,'ruckusWLINKIISSID':ruckusWLINKIISSID,'ruckusWLINKIIRole':ruckusWLINKIIRole,'ruckusWLINKIILocalMAC':ruckusWLINKIILocalMAC,'ruckusWLINKIIRemoteMAC':ruckusWLINKIIRemoteMAC,'ruckusWLINKIITxPkts':ruckusWLINKIITxPkts,'ruckusWLINKIITxBytes':ruckusWLINKIITxBytes,'ruckusWLINKIIRxPkts':ruckusWLINKIIRxPkts,'ruckusWLINKIIRxBytes':ruckusWLINKIIRxBytes,'ruckusWLINKIIEstablishTime':ruckusWLINKIIEstablishTime,'ruckusWLINKIIUpTime':ruckusWLINKIIUpTime,'ruckusWLINKIIRssi':ruckusWLINKIIRssi,'ruckusWLINKIIUpCount':ruckusWLINKIIUpCount,'ruckusWLINKIIDownCount':ruckusWLINKIIDownCount,'ruckusWLINKEvents':ruckusWLINKEvents})