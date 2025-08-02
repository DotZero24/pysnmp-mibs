_I='s5EnPIntconPortIndx'
_H='s5EnPIntconBrdIndx'
_G='s5EnPIntconIfIndx'
_F='read-write'
_E='TimeIntervalSec'
_D='read-only'
_C='S5-ETHERNET-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
s5Eth,=mibBuilder.importSymbols('S5-ROOT-MIB','s5Eth')
TimeIntervalSec,=mibBuilder.importSymbols('S5-TCS-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
s5EthernetMib=ModuleIdentity((1,3,6,1,4,1,45,1,6,6,0))
if mibBuilder.loadTexts:s5EthernetMib.setRevisions(('2004-07-20 00:00',))
_S5EnCfg_ObjectIdentity=ObjectIdentity
s5EnCfg=_S5EnCfg_ObjectIdentity((1,3,6,1,4,1,45,1,6,6,1))
_S5EnStat_ObjectIdentity=ObjectIdentity
s5EnStat=_S5EnStat_ObjectIdentity((1,3,6,1,4,1,45,1,6,6,2))
_S5EnMisc_ObjectIdentity=ObjectIdentity
s5EnMisc=_S5EnMisc_ObjectIdentity((1,3,6,1,4,1,45,1,6,6,3))
_S5EnPIntconTable_Object=MibTable
s5EnPIntconTable=_S5EnPIntconTable_Object((1,3,6,1,4,1,45,1,6,6,3,1))
if mibBuilder.loadTexts:s5EnPIntconTable.setStatus(_A)
_S5EnPIntconEntry_Object=MibTableRow
s5EnPIntconEntry=_S5EnPIntconEntry_Object((1,3,6,1,4,1,45,1,6,6,3,1,1))
s5EnPIntconEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:s5EnPIntconEntry.setStatus(_A)
class _S5EnPIntconIfIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_S5EnPIntconIfIndx_Type.__name__=_B
_S5EnPIntconIfIndx_Object=MibTableColumn
s5EnPIntconIfIndx=_S5EnPIntconIfIndx_Object((1,3,6,1,4,1,45,1,6,6,3,1,1,1),_S5EnPIntconIfIndx_Type())
s5EnPIntconIfIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnPIntconIfIndx.setStatus(_A)
class _S5EnPIntconBrdIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPIntconBrdIndx_Type.__name__=_B
_S5EnPIntconBrdIndx_Object=MibTableColumn
s5EnPIntconBrdIndx=_S5EnPIntconBrdIndx_Object((1,3,6,1,4,1,45,1,6,6,3,1,1,2),_S5EnPIntconBrdIndx_Type())
s5EnPIntconBrdIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnPIntconBrdIndx.setStatus(_A)
class _S5EnPIntconPortIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_S5EnPIntconPortIndx_Type.__name__=_B
_S5EnPIntconPortIndx_Object=MibTableColumn
s5EnPIntconPortIndx=_S5EnPIntconPortIndx_Object((1,3,6,1,4,1,45,1,6,6,3,1,1,3),_S5EnPIntconPortIndx_Type())
s5EnPIntconPortIndx.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnPIntconPortIndx.setStatus(_A)
class _S5EnPIntconIntconStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('interconnect',2)))
_S5EnPIntconIntconStatus_Type.__name__=_B
_S5EnPIntconIntconStatus_Object=MibTableColumn
s5EnPIntconIntconStatus=_S5EnPIntconIntconStatus_Object((1,3,6,1,4,1,45,1,6,6,3,1,1,4),_S5EnPIntconIntconStatus_Type())
s5EnPIntconIntconStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s5EnPIntconIntconStatus.setStatus(_A)
class _S5EnPIntconAddrCollect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('neverCollect',2),('alwaysCollect',3)))
_S5EnPIntconAddrCollect_Type.__name__=_B
_S5EnPIntconAddrCollect_Object=MibTableColumn
s5EnPIntconAddrCollect=_S5EnPIntconAddrCollect_Object((1,3,6,1,4,1,45,1,6,6,3,1,1,5),_S5EnPIntconAddrCollect_Type())
s5EnPIntconAddrCollect.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnPIntconAddrCollect.setStatus(_A)
class _S5EnNodeInactInterval_Type(TimeIntervalSec):defaultValue=5;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5EnNodeInactInterval_Type.__name__=_E
_S5EnNodeInactInterval_Object=MibScalar
s5EnNodeInactInterval=_S5EnNodeInactInterval_Object((1,3,6,1,4,1,45,1,6,6,3,2),_S5EnNodeInactInterval_Type())
s5EnNodeInactInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnNodeInactInterval.setStatus(_A)
class _S5EnNodeAgeInterval_Type(TimeIntervalSec):defaultValue=300;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_S5EnNodeAgeInterval_Type.__name__=_E
_S5EnNodeAgeInterval_Object=MibScalar
s5EnNodeAgeInterval=_S5EnNodeAgeInterval_Object((1,3,6,1,4,1,45,1,6,6,3,3),_S5EnNodeAgeInterval_Type())
s5EnNodeAgeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:s5EnNodeAgeInterval.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'s5EthernetMib':s5EthernetMib,'s5EnCfg':s5EnCfg,'s5EnStat':s5EnStat,'s5EnMisc':s5EnMisc,'s5EnPIntconTable':s5EnPIntconTable,'s5EnPIntconEntry':s5EnPIntconEntry,_G:s5EnPIntconIfIndx,_H:s5EnPIntconBrdIndx,_I:s5EnPIntconPortIndx,'s5EnPIntconIntconStatus':s5EnPIntconIntconStatus,'s5EnPIntconAddrCollect':s5EnPIntconAddrCollect,'s5EnNodeInactInterval':s5EnNodeInactInterval,'s5EnNodeAgeInterval':s5EnNodeAgeInterval})